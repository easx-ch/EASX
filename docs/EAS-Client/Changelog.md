This document contains all changes made to EAS Client application.

### 2.1.0 - 2025-09-22

- Added: Introduced **transparency logs** to increase end-to-end encryption security with tamper-evidence [#508]
- Added: Volumes for persistent files needed in docker (Logs, Data) [#536]
- Added: Extra button in UI for download PDF in details of incoming document [#521]
- Added: Minor improvements in the EAS Client UI (loaders, toaster notifications for long request, etc.)
- Fixed: name space issues when migrating between schema versions [#537]
- Fixed: PDF rendering when document version isn't FZL 1.6 [#537]
- Fixed: on startup EAS Client UI and APIs were blocked until all documents were loaded when using document cache
- Removed: previously depreciated endpoints (migration-scripts and xml-schemas) in directory service

### 2.0.2 - 2025-07-02

- Added: Examples for creating entry/exit on client side (Swagger)
- Added: Set `Content-Security-Policy: frame-ancestors 'none'` [#520 g14]
- Added: Add `X-Content-Type-Options: nosniff` header [#518 g12]
- Updated: Use newest .NET Ubuntu image [#505 g1/g2]
- Updated: Allow higher moduli of private key [#510 g7]

### 2.0.1 - 2024-12-05

- Fixed: Corrected the OpenAPI (Swagger) documentation to show the correct error response type for EAS Client's Matching Service endpoints [#499]
- Fixed: When CertificatePassword is set configuring CertificateContent is needed even though CertificatePath is set [#494]
- Remove unnecessary certificates in docker image [#491]

### 2.0.1 - 2024-12-05

- Fixed: Corrected the OpenAPI (Swagger) documentation to show the correct error response type for EAS Client's Matching Service endpoints [#499]
- Fixed: When CertificatePassword is set configuring CertificateContent is needed even though CertificatePath is set [#494]
- Remove unnecessary certificates in docker image [#491]

### 2.0.0 - 2024-10-25

#### New Services & Features
- Retrieve **FZL documents as PDF** [#355]
- **WAK Service** allowing submitting reinstatement notifications (WAK = Wiederanschlusskontrolle) to AEIS [#351]
- New **requiredVersion** parameter in client Hub API GET /in-documents/{id} to define FZL-Schema version needed [#437]
- Auto-updating of validations and migration scripts, to improve future backward-compatibility [#444]

#### Changes
- Removed Matching Service logs [#460]
- Reduced size of EAS Client Docker images [#453]

#### Bugs
- Removed multiple critical **vulnerabilities in Docker images** for EAS Client [#453]
- Fixed: Featureflags are being retrieved from server in EASClient every time we get document [#446]
- Fixed: TransferSenderId is empty in the Deleting document request
- Fixed: response for creating entries\exits did not return ID [#452]

### 1.2.2 - 2024-04-11
- Fixed: Error on deleting document with message when transferSenderId is not set. 

### 1.2.1 - 2024-03-05
- Fixed: Not using the overriding participant configuration (Patch from 1.0.1)
- Validating the content of the XML document during sending and receiving (Disabled by default)

### 1.2.0 - 2024-02-07
- Revoke sent document functionality 
- fixed: Document not removed from cache when deleted

### 1.1.1 - 2024-01-25
- Fixed: Log view not showing correctly (since V1.1.0)
- Group EAS Client API in Hub, Directory and Matching
- Retrieval of Matching Service Logs using GET HTTP command
- Update to .net 8

### 1.1.0 - 2024-01-11
- Encrypting receipts
- Introduce a matching service
- Set documenttype independent of FZL schema version to "http://exchange.aeis.ch/xsd/FZL"
- Fix missing Data Migration tag

### 1.0.1 - 2024-02-28 (Release Patch)
- Fixed: Not using the overriding participant configuration (certificate, private key)

### 1.0.0 - 2023-09-19

- FZL 1.6 support
- Extended documentation for document caching and searching using XPath
- Fixed issues when sending documents without UID of sender
- Fixed: XPath filtering doesn't work with default namespace of FZL-Schema 1.6

### 0.9.3 - 2023-03-31

- Extend `ReceiptDTO` with `State` property (`Read`,`Deleted`);
- Add new type of receipt "Read", which is sent automatically, when user tries to retrieve document by id;
- Extend `DocumentMessageMinimalDto` with `State` property (`Sent`, `Read`, `Deleted`), `UpdatedOn` property `Datetime`;
- Extend `DocumentMessage` with `State` property (`Sent`, `Read`, `Deleted`), `UpdatedOn` property `Datetime`;
- Implement document storage service (cache service), add new  [EAS Client Settings](Settings.md) properties `DocumentCacheMode` (default `Disabled`) and SyncDocumentsIntervalMinutes (default `5`). 
- Introduced searching incoming documents by XPath.

### 0.9.2 - 2022-12-19

- Migrate from .Net 5 to .Net 7;
- Implement an ability to support document migration and validation for new FZL-Schemas without updating to new client versions;

### 0.9.1.1 - 2022-10-10

- Fixed: senderId ignored for retrieving override configuration when signing before sending

### 0.9.1 - 2022-04-11

- Implement ability to upload certificates and private keys and storage them as base64 string;
- Implement ability to secure configuration;
- Implement ability to edit settings in JSON editor;

### 0.9.0 - 2022-04-04

- Implement ability to validate outgoing and incoming documents;
- Implement ability to migrate a document to a specific version;
- Automatically send failed receipts when use command `--recieve folderName`;
- Update favicons with a new logo;
- Improve a configuration section;

### 0.8.8.3 - 2022-03-22

- Implement ability to renew a private/public key;
- Implement ability to renew a certificate;

### 0.8.8.2 - 2022-03-17

- Fix bug:  Anyone can send to BVG Exchange participant with wrong Sender UID;

### 0.8.8.1 - 2022-03-10

- Fix bug: Swagger not working in docker EASClient;

### 0.8.8 - 2022-02-08

- WEB GUI: improve styling for different themes;
- Support FZL V1.5;
- Support configuring mutliple subscriptionkey/privatekeys on EAS Client;
- Allow user to switch participant shown in EAS Client;
- Improve API error handling;

### 0.8.7 - 2021-12-24

- WEB GUI: improve registration flow;
- WEB GUI: implement field validation for registration page;
- WEB GUI: imrpove notification;
- Fix bug with fetching IDs from .xml file
- Move toggle for changing theme to the navigation bar.
- --generatekeys name - fix unexpected errors.
- Implement urls according to current environment.

### 0.8.6 - 2021-11-24

- WEB GUI: registration 

### 0.8.5 - 2021-08-18

- Support of multiple platforms and architectures
- Use Client Certificates from storage, in addition to file system
- Web GUI: dark mode
- Web GUI: preview buttons in lists

### 0.8.4 - 2021-08-06

- Web GUI: document and receipt management
- Web GUI: participants overview
- Web GUI: document logs with graphical previews for new operations
- Web GUI: client settings
- `--debug` parameter
- `--host` command does not print verbose logs by default
- New API endpoint `https://api.easx.ch`

### 0.8.0 - 2021-06-06

- Initial release
