# Monitoring the EAS Client

When running in host mode, the EAS Client exposes endpoints to verify availability and collect runtime metrics.

## Health Endpoints

Two health endpoints are available:

| Endpoint            | Purpose                                                                       |
| ------------------- | ----------------------------------------------------------------------------- |
| `GET /health/live`  | Liveness — is the process running and able to respond?                        |
| `GET /health/ready` | Readiness — is the client configured correctly and ready to process requests? |

Both endpoints return JSON and use standard HTTP status codes: `200` when healthy, `503` when not.

### Liveness

```sh
curl http://localhost:5000/health/live
```

```json
{
  "status": "Healthy",
  "version": "2.1.0",
  "checks": []
}
```

Use this to confirm the EAS Client process is alive and the web host is responding. It has no dependencies — a `200` response means the HTTP stack is up.

### Readiness

```sh
curl http://localhost:5000/health/ready
```

```json
{
  "status": "Healthy",
  "version": "2.1.0",
  "checks": [
    {
      "name": "configuration",
      "status": "Healthy",
      "description": "Configuration is valid"
    }
  ]
}
```

Use this to confirm the EAS Client is correctly configured and ready to handle requests. If the configuration is missing or invalid, the endpoint returns `503`:

```json
{
  "status": "Unhealthy",
  "version": "2.1.0",
  "checks": [
    {
      "name": "configuration",
      "status": "Unhealthy",
      "description": "Configuration is invalid or incomplete"
    }
  ]
}
```

This distinction is useful for quickly determining whether an issue originates from the client itself or from its configuration.

### Docker and Kubernetes

For Docker, use `/health/live` as the `HEALTHCHECK` target. For Kubernetes, map `/health/live` to the `livenessProbe` and `/health/ready` to the `readinessProbe`.

## Correlation ID

Every incoming request (other than the health endpoints above) is assigned a correlation ID, used to tie together all log entries produced while handling that request — useful when tracing a single request across the EAS Client and the systems it talks to.

- If the request includes an `X-Correlation-ID` header, that value is used.
- If it's absent (or empty), the EAS Client generates a new one.
- The value is returned on the response as `X-Correlation-ID`, and included as the `CorrelationId` field on every structured log entry produced while handling the request.
- Requests forwarded to plugins via the reverse proxy carry the same correlation ID, so a request that crosses into a plugin and back keeps its correlation ID throughout.

```sh
curl -i -H "X-Correlation-ID: my-request-id" http://localhost:5000/some-endpoint
```

```
HTTP/1.1 200 OK
X-Correlation-ID: my-request-id
...
```

If no `X-Correlation-ID` header is sent, the response header instead contains a generated GUID.

## Metrics Endpoint

```
GET http://localhost:9090/metrics
```

The metrics endpoint is exposed on a **dedicated internal port** (default: `9090`), separate from the public API port. It is not reachable via the public API. This is intentional. Accessing `/metrics` on the API port returns `404`.

The port is configurable via the `MetricsPort` setting in your configuration file.

The endpoint exposes runtime metrics in Prometheus / OpenMetrics text format, compatible with any platform that supports Prometheus scraping: Prometheus, Datadog, Azure Monitor, Grafana Cloud, and others.

### Plugin Metrics

These metrics are specific to the EAS Client and are the most useful for dashboards and alerting.

| Metric                                 | Type      | Description                                                                                                                    |
| -------------------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------ |
| `easx_plugin_requests_total`           | Counter   | Requests proxied to each plugin, labelled by `plugin`, `method`, and `status` (`success` / `error`)                            |
| `easx_plugin_request_duration_seconds` | Histogram | Request latency per plugin — use this to detect slow or degraded plugins                                                       |
| `easx_plugin_errors_total`             | Counter   | Errors per plugin, labelled by `error_type` (`upstream_error` for plugin 5xx responses, `proxy_error` for connection failures) |
| `easx_plugin_lifecycle_events_total`   | Counter   | Plugin lifecycle events labelled by `plugin` and `event` (`started`, `stopped`, `crashed`, `health_failed`)                    |

Example output after traffic has been processed:

```
easx_plugin_requests_total{plugin="fzlhub",method="POST",status="success"} 142
easx_plugin_requests_total{plugin="fzlhub",method="POST",status="error"} 3
easx_plugin_request_duration_seconds_bucket{plugin="fzlhub",le="0.1"} 138
easx_plugin_errors_total{plugin="fzlhub",error_type="upstream_error"} 3
easx_plugin_lifecycle_events_total{plugin="fzlhub",event="started"} 1
easx_plugin_lifecycle_events_total{plugin="fzlhub",event="crashed"} 0
```

> **Note:** Plugin request metrics (`easx_plugin_requests_total`, `easx_plugin_request_duration_seconds`, `easx_plugin_errors_total`) only appear after the first request has been proxied to that plugin. Lifecycle metrics appear immediately on startup.

### HTTP Server Metrics

| Metric                          | Type      | Description                                  |
| ------------------------------- | --------- | -------------------------------------------- |
| `http_requests_received_total`  | Counter   | Total requests handled by the EAS Client API |
| `http_request_duration_seconds` | Histogram | API request latency                          |
| `http_requests_in_progress`     | Gauge     | Currently active requests                    |

### Process and Runtime Metrics

| Metric                                           | Description                                                              |
| ------------------------------------------------ | ------------------------------------------------------------------------ |
| `process_cpu_seconds_total`                      | Cumulative CPU time — use the rate to see current CPU usage              |
| `process_working_set_bytes`                      | Physical memory in use — useful for detecting memory growth over time    |
| `dotnet_collection_count_total`                  | GC collection counts by generation — gen2 collections are expensive      |
| `system_runtime_dotnet_thread_pool_thread_count` | Thread pool size — sustained growth may indicate thread starvation       |
| `system_runtime_dotnet_gc_pause_time`            | Total time spent in GC pauses — relevant for latency-sensitive workloads |
