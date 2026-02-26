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
 -v /c/easx/dockertest/Logs:/Logs \
 -v /c/easx/dockertest/Data:/Data \
 easx/client:latest-test
```

**Explanation:**

- `-p 5000:80` exposes the EAS Client API and GUI on port 8080.
- `-e ...` sets environment variables for configuration (see [Settings](./Settings.md)).
- `-v /c/easx/dockertest/Logs:/Logs` mounts the host volume directory `/Logs` to the container's log directory at `C:\easx\dockertest\Logs`.
- `-v /c/easx/dockertest/Data:/Data` mounts the host volume directory `/Data` to the container's data directory at `C:\easx\dockertest\Data`.
- `easx/client:latest-test` specifies the image and tag to use.
- In this example the client ceritificate and private key are stored in respective files under `C:\easx\dockertest\Data\Config`

**Access the EAS Client:**

- Open [http://localhost:5000](http://localhost:5000) in your browser to access the API and GUI.

**Check Logs and Data:**

- Logs will be written to `C:\easx\dockertest\Logs` on your host.
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

- `/Logs`: Stores log files written by the EAS Client.
- `/Data`: Stores persistent data, such as cached documents (if enabled) and participant transparency log audit entries.

Mount these volumes to host directories to persist logs and data outside the container.

**NOTE:** It is strongly recommended to map these volumes so that the cached data, logs and entries for transparency log audits is not lost on restarting the docker instance.

## Configuration via Environment Variables

All EAS Client settings can be passed as environment variables. This is the recommended approach for Docker deployments.

For a full list and details, see [Settings](Settings.md).

Please note that the following defaults are overriden by the docker image to support persisting using the available volumes above:
- `LogsPath` is set to `/Logs`
- `LoggedKeysPath` is set to `/Data/LoggedKeys`
- `CachePath` is set to `/Data/Cache/`

## Best Practices

- Always use the recommended tag from the [EASX Portal](https://portal.easx.ch).
- Mount the `/Logs` and `/Data` volumes to persist logs and data.
- Pass all sensitive settings as environment variables or use secure secrets management (e.g., Azure Key Vault).
- For production, use the `latest` tag; for testing, use `latest-test`.
- Regularly check logs for errors or warnings.

## Troubleshooting

- Use `docker logs eas-client` to view application logs.
- Ensure all required environment variables are set; missing required values will prevent startup.
- Check the [EASX Portal](https://portal.easx.ch) for the current recommended image tag.
- For connectivity issues, verify your firewall and port mappings.

## Further Reading

- [EAS Client Introduction](Introduction.md)
- [Settings Reference](Settings.md)
- [Deploy to Azure](Deploy-To-Azure.md)
- [Docker Hub: easx/client](https://hub.docker.com/r/easx/client)
- [EASX Portal](https://portal.easx.ch)
