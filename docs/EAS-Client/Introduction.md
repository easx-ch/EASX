# EAS Client Overview

The **EAS Client** encapsulates essential functionalities for accessing **EASX**, including robust handling of security and compatibility features to ensure end-to-end encryption.

## Deployment Options

The EAS Client is available in two deployment options:

### 1. Executable File

The binary executable file can be downloaded from the [EASX portal](https://portal.easx.ch) upon signing in. Versions are available for Windows, Linux, and macOS.

The EAS Client is a self-contained, single-file application requiring no additional dependencies. It can be placed in a directory and configured as explained in [Settings](Settings.md).

### 2. Docker Image

The EAS Client is also available as a [Docker image](https://hub.docker.com/r/easx/client) on Docker Hub, allowing for easy deployment and management of access to EASX. Configuration options support the use of secure key repositories (e.g., Azure Key Vault).

See [Docker Usage and Configuration](Docker.md) for detailed instructions, available tags, volumes, and environment variable setup.

For an example of using the EAS Client as a Docker instance deployed on Azure App Service, see [Deploy to Azure](Deploy-To-Azure.md).

## Functionality

Once set up, the EAS Client supports multiple interaction methods:

### 1. Client API Requests

This is the primary approach to using of the EAS Client. This allows applications to integrate into the EASX platform using the EAS API without having to implement encryption, signing, and validation themselves. When the EAS Client is run in host mode, it launches a local instance of the EAS API that handles security. To run the EAS Client in host mode:

`EASClient.exe --host`

In this mode the EAS Client provides a RESTful API and you can send simple, unencrypted HTTP requests to the local client URL. The EAS Client will validate the request and handle payload encryption, signature generation, attaching subscription headers and client certificate, specifying default UID and securly communicating with the EASX server. Upon receiving a response, it will validate the signature, decrypt the payload, and return the decrypted response.

To ease the implementation into your application an OpenAPI Specification is available.

### 2. Client GUI

For manually exchanging documents, viewing logs, configuring EAS Client settings, or experimenting with the local API, consider using the GUI. When running the EAS Client in host mode (`EASClient.exe --host`), it launches a local instance of the EAS Client GUI (next to the Client API) accessible from a browser.

The GUI allows you to send, view, and manage documents and receipts, access the client directory, view logs, and more. It also includes Swagger and an OpenAPI Specification, making it easy to try out the local API.

This option is ideal for users who prefer a manual approach. For instance, you can create a shortcut to launch the EAS Client in hosted mode, open the Incoming Documents page in your browser, and download a document without needing to manage encryption or command-line instructions.
For details on using the Transparency Logs Page, see [Transparency Logs Page (UI Usage)](Transparency-Logs-UI.md).

### 3. Command-Line Scripts

A full list of supported commands is documented under [EAS Client Commands](Commands.md). For example:

- To receive all incoming documents into a specified folder, run:

  `EASClient.exe --receive "incoming folder"`

  This command also handles additional tasks such as sending receipts.

- To send a document, copy it into the specified folder and run:

  `EASClient.exe --send "outgoing folder"`

You can automate these commands using batch/shell scripts configured to run periodically with Windows Task Scheduler or a cron job.

> **Note**: Command-line scripts are only available when the EAS Client is deployed as an executable file, not as a Docker instance.

## Caching and Filtering Incoming Documents

The EAS Client provides options for local caching of incoming documents, allowing you to retrieve documents from the server and store them locally for later processing. Additionally, it provides an extension to the EASX Hub API to retrieve a filtered list of FZL documents using an XPath expression. This feature is useful when documents do not need to be processed immediately upon retrieval. For more details, see [Filtering Using XPath](Filter-Using-XPath.md).

## Retrieving Incoming Documents as PDFs

The EAS Client also supports retrieving incoming documents as PDFs, which is beneficial for presenting data in a human-readable format. For more information, see [Retrieving as PDF](Retrieve-PDF.md).
