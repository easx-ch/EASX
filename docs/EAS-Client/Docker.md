# EAS Client Docker Image

The EAS Client is available as a Docker image for easy deployment and management. This page provides details on usage, configuration, available tags, volumes, and best practices.

## Docker Hub

The EAS Client docker hub images can be retrieved from the Docker Hub at [easx/client](https://hub.docker.com/r/easx/client).

## Tags

- `latest`: Use this tag for production deployments. It always points to the latest stable release.
- `latest-test`: Use this tag for test environments. It points to the latest version intended for testing.
- `latest-dev`: Internal/development tag, not relevant for customers.

Use the versioned tags (i.e. "2.0.2") to use a fixed version.

> **Note:** The currently recommended tag for test or production is shown on the [EASX Portal](https://portal.easx.ch).

## Usage Example

The following is an example of starting the docker instance.

The paths on the right-hand side of the volume mappings are paths inside the
container. `/Data` and `/Logs` are the recommended fixed mount targets; the
customer can choose any suitable paths on the host on the left-hand side.

```sh
docker run -d \
 --name eas-client \
 -p 5000:80 \
 -e Environment=test \
 -e ParticipantId=CHE123456789 \
 -e EasxSubscriptionKey=your_subscription_key \
 -e PrivateKeyPath=/Data/Config/your-private_key.pem \
 -e CertificatePath=/Data/Config/your-client_certificate.p12 \
 -e CertificatePassword= \
 -e PluginProfile=standard \
 -v /c/easx/dockertest/Logs:/Logs \
 -v /c/easx/dockertest/Data:/Data \
 easx/client:latest-test
```

**Explanation:**

- `-p 5000:80` exposes the EAS Client API and GUI on port 5000.
- `-e ...` sets environment variables for configuration (see [Settings](./Settings.md)).
- `PluginProfile=standard` starts the usual FZL Hub, Matching, and WAK plugins. This is also the default for a fresh configuration.
- `-v /c/easx/dockertest/Logs:/Logs` mounts the host directory `/c/easx/dockertest/Logs` at the container path `/Logs`.
- `-v /c/easx/dockertest/Data:/Data` mounts the host directory `/c/easx/dockertest/Data` at the container path `/Data`.
- `easx/client:latest-test` specifies the image and tag to use.
- In this example the client certificate and private key are stored in respective files under `C:\easx\dockertest\Data\Config`.

**Access the EAS Client:**

- Open [http://localhost:5000](http://localhost:5000) in your browser to access the API and GUI.

**Check Logs and Data:**

- With the default Docker logging configuration, application logs of level `Warning` and above are available through `docker logs eas-client` and as rolling files under `C:\easx\dockertest\Logs` on the host.
- Persistent data (such as cached documents and transparency logs) will be stored in `C:\easx\dockertest\Data`.

**Stopping and Managing the Container:**

- To stop the container:  
  `docker stop eas-client`
- To start it again:  
  `docker start eas-client`
- To view logs:  
  `docker logs eas-client`

**Example of deployment to Azure App Service**

For an example of using the EAS Client as a Docker instance deployed on Azure App Service, see [Deploy to Azure](Deploy-To-Azure.md).

## Available Volumes

- `/Logs`: Stores rolling application log files written by the EAS Client. With the default Docker logging configuration, the same events are also sent to stdout and can be viewed with `docker logs`.
- `/Data`: Stores persistent data, such as cached documents (if enabled) and participant transparency log audit entries.

The container runs as a non-root user. The image provides these mount points in
advance, so the application does not need to create arbitrary directories in
the restricted base image. Create host bind-mount directories before starting
the container and make sure they are writable by the container user.

Mount these volumes to host directories or named Docker volumes to persist logs
and data outside the container. The host paths can be changed without changing
the container paths:

```sh
docker run -d \
  --name eas-client \
  -p 5000:80 \
  --mount type=bind,source=/srv/eas/data,target=/Data \
  --mount type=bind,source=/srv/eas/logs,target=/Logs \
  easx/client:latest
```

**NOTE:** It is strongly recommended to map these volumes so that the cached data, logs and entries for transparency log audits is not lost on restarting the docker instance.

## Configuration via Environment Variables

All EAS Client settings can be passed as environment variables. This is the recommended approach for Docker deployments.

For a full list and details, see [Settings](Settings.md).

Fresh deployments use `PluginProfile=standard` by default. To start only explicitly configured plugins, set `PluginProfile=custom` and provide `Plugins__{pluginId}__Version` or other plugin settings as needed.

Please note that the following defaults are overridden by the docker image to support persisting using the available volumes above:
- `LogsPath` is set to `/Logs`
- `LoggedKeysPath` is set to `/Data/LoggedKeys`
- `CachePath` is set to `/Data/Cache/`

These are container paths, not host paths. Do not set them to an arbitrary host
path. To use a different persistent location, change the host side of the
`--mount` or `-v` mapping and keep `/Data` and `/Logs` as the container targets.

## Best Practices

- Always use the recommended tag from the [EASX Portal](https://portal.easx.ch).
- Mount the `/Logs` and `/Data` volumes to persist logs and data.
- Create bind-mount directories before starting the container and verify that
  the container user can write to them.
- Keep both log destinations available: use `docker logs` for container output
  and the mounted `/Logs` directory for rolling log files.
- Pass all sensitive settings as environment variables or use secure secrets management (e.g., Azure Key Vault).
- For production, use the `latest` tag; for testing, use `latest-test`.
- Regularly check logs for errors or warnings.

## Troubleshooting

- Use `docker logs eas-client` to view application logs.
- With the default Docker logging configuration, file logs are written as
  `logYYYYMMDD.txt` in the configured `LogsPath`. The default Docker path is
  `/Logs`, and a file is created when an event of level `Warning` or above is
  emitted.
- If `SerilogHost` is configured, it replaces the default logging sinks and
  levels. Add both `Console` and `File` sinks explicitly when both destinations
  are required. For a Docker file sink, use a writable path under `/Logs`, for
  example `/Logs/log.txt`.
- Do not delete an active rolling log file directly from the host. The process
  may continue writing to the already opened Linux file handle, while the file
  remains invisible on the host. Restart the container to reopen and recreate
  the file.
- Ensure all required environment variables are set; missing required values will prevent startup.
- Check the [EASX Portal](https://portal.easx.ch) for the current recommended image tag.
- For connectivity issues, verify your firewall and port mappings.

## Further Reading

- [EAS Client Introduction](Introduction.md)
- [Settings Reference](Settings.md)
- [Deploy to Azure](Deploy-To-Azure.md)
- [Docker Hub: easx/client](https://hub.docker.com/r/easx/client)
- [EASX Portal](https://portal.easx.ch)
