# EAS Client Plugins

## What Are Plugins?

The EAS Client is built as an extensible platform. **Plugins** are independently versioned service modules that extend the client with additional business capabilities. They run as separate processes under the supervision of the EAS Client host, but from your perspective — and from the perspective of integrating systems — they appear as part of a single, unified application.

This means:

- One URL, one API, one Swagger specification
- One UI with navigation across all available services
- One set of configuration files and environment variables
- One Docker image to deploy and maintain

Plugins are updated independently of the host. When a plugin receives an update, only that component changes; the host and other plugins continue running unchanged.

---

## Standard Plugins

The **standard plugin profile** (the default) starts the following plugins automatically:

| Plugin | ID | Description |
|---|---|---|
| **FZL Hub** | `fzlhub` | Receives and processes FZL documents from EASX. Provides document storage, retrieval, and status tracking. |
| **Matching** | `matching` | Matching service for pension fund data. |
| **WAK** | `wak` | WAK (Auffangeinrichtung) integration for forwarding documents to the WAK platform. |

Additional plugins (ELM Receiver, PKData) are available and can be enabled via configuration.

---

## Plugin APIs and UI

Each plugin exposes its REST API under a versioned base path:

```
/api/{plugin-id}/v{major}/...
```

Examples:

- `GET /api/eas/v1/documents`
- `POST /api/matching/v1/jobs`

All plugin APIs are included in the combined Swagger specification available at `/swagger`.

Plugin UIs are accessible through the host shell navigation and embedded at `/app/p/{plugin-id}/`.

---

## Controlling Which Plugins Start

### PluginProfile

The `PluginProfile` setting determines which plugins are started:

| Value | Behaviour |
|---|---|
| `standard` *(default)* | Starts FZL Hub, Matching, and WAK at their current versions |
| `custom` | Starts only the plugins explicitly listed under `Plugins` |

Example — use the standard profile with all defaults:

```json
{
  "PluginProfile": "standard"
}
```

Example — start only FZL Hub:

```json
{
  "PluginProfile": "custom",
  "Plugins": {
    "fzlhub": {}
  }
}
```

### Disabling an individual plugin

To keep the standard profile but disable one plugin:

```json
{
  "PluginProfile": "standard",
  "Plugins": {
    "wak": {
      "Enabled": false
    }
  }
}
```

### Pinning a specific plugin version

```json
{
  "PluginProfile": "standard",
  "Plugins": {
    "matching": {
      "Version": "1.2.3"
    }
  }
}
```

---

## Plugin-Specific Settings (PluginSettings)

Each plugin has its own settings namespace. Use `PluginSettings` to pass configuration to a specific plugin:

```json
{
  "PluginSettings": {
    "fzlhub": {
      "DocumentCacheMode": "Enabled",
      "SyncDocumentsIntervalMinutes": 10
    }
  }
}
```

Settings under `PluginSettings.{plugin-id}` are injected into the plugin process as environment variables. The available keys differ per plugin; refer to the plugin's own documentation for its supported settings.

### FZL Hub settings

| Setting | Default | Description |
|---|---|---|
| `DocumentCacheMode` | `Disabled` | Document cache mode: `Disabled`, `EnabledWithoutPrefetch`, or `Enabled` |
| `SyncDocumentsIntervalMinutes` | `5` | How often the cache sync task runs, in minutes |

> **Note:** `DocumentCacheMode` and `SyncDocumentsIntervalMinutes` were previously top-level settings in `EASClient.settings.json`. They are now configured per-plugin via `PluginSettings` and the top-level keys are deprecated.

---

## Plugin Status and Management

When the EAS Client is running in host mode, you can check the status of all plugins:

```
GET /api/plugins
```

Response includes each plugin's ID, version, status (`Running`, `Stopped`, `Disabled`, `Failed`), registered endpoints, and any routing conflicts.

Individual plugin operations:

| Request | Effect |
|---|---|
| `GET /api/plugins/{id}` | Status and endpoint details for one plugin |
| `POST /api/plugins/{id}/start` | Start a stopped plugin |
| `POST /api/plugins/{id}/stop` | Stop a running plugin |
| `POST /api/plugins/{id}/restart` | Restart a plugin |
| `POST /api/plugins/{id}/deactivate` | Stop and permanently disable automatic startup for a plugin |
| `POST /api/plugins/{id}/activate` | Re-enable and start a deactivated plugin |
| `DELETE /api/plugins/{id}` | Stop, remove all installed versions, and remove the plugin from the local registry |

Deactivation is persisted in the local plugin registry and survives a client restart. Removal deletes only installed plugin artifacts under the configured plugin root; a plugin that is still included by the `standard` profile can be downloaded again on a later startup, so use deactivation when it must remain disabled.

---

## Health and Readiness

The EAS Client exposes two health endpoints:

| Endpoint | Purpose | Plugin behaviour |
|---|---|---|
| `GET /health/live` | Liveness — is the process up? | Not checked; always healthy while the process runs |
| `GET /health/ready` | Readiness — is the host ready to serve traffic? | Returns `unhealthy` if any enabled plugin is not `Running` or has no registered endpoints |

A plugin that fails to start or times out during endpoint registration is marked `Failed` in the registry. This does not affect liveness, but the readiness endpoint returns `unhealthy` until all enabled plugins are running. The response body includes which plugins are not ready and why (e.g. `matching: Failed (timeout)`).

Container orchestrators (Kubernetes, Azure App Service) should use `/health/live` for the liveness probe and `/health/ready` for the readiness probe.

---

## Relevant Settings Reference

These host-level settings control the plugin runtime. See [Settings](Settings.md) for the full parameter reference.

| Setting | Default | Description |
|---|---|---|
| `PluginProfile` | `standard` | Which plugin set to start |
| `PluginControlPort` | `5005` | Internal gRPC control port (no need to change in normal use) |
| `PluginRegistrationTimeoutSeconds` | `10` | How long the host waits for a plugin to register after starting |
| `Plugins` | — | Per-plugin overrides (version, enabled, development path) |
| `PluginSettings` | — | Per-plugin configuration dictionary |

---

## Docker Considerations

When running as a Docker container, plugin storage directories are under the data volume. To preserve plugin state and avoid re-initialization on container restart, mount the data volume:

```yaml
volumes:
  - easx-data:/data
```

Per-plugin settings are best passed as environment variables:

```yaml
environment:
  EASX_PLUGIN__FZLHUB__DOCUMENTCACHEMODE: "Enabled"
```

The environment variable prefix for a plugin with ID `my-plugin` is `EASX_PLUGIN__MY_PLUGIN__` (uppercase, hyphens replaced with underscores).
