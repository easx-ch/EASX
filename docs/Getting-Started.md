The following guide will help you get up and running in a test environment using the EAS Client installed locally.

# Registering account and subscription

To connect to EASX you will need to have an appropriate developer account and product subscription. This can be applied for on the [EASX developer portal](https://portal.easx.ch/):

- Open the developer portal in your browser: https://portal.easx.ch
- Go to the [signup page](https://portal.easx.ch/signup)
- Enter the required information and press the "Sign up" button
- You will receive an email you need to confirm
- [Signin](https://portal.easx.ch/signin) with your new account
- On the [products page](https://portal.easx.ch/products) select the [EASX Test](https://portal.easx.ch/product#product=easx-test) product
- Apply for a new subscription by entering a name for this subscription and pressing the "Subscribe" button
- You will find your new subscription on the [profile page](https://portal.easx.ch/profile), press the "Show" link next to the primary key and copy the key. You will need it later.
- Generate an RSA key pair (3072-bit by default, 4096-bit optional) and store them as separate `.pem` files. We highly recommend using the EAS Client for key generation, as it allows specifying the key size. To generate keys, download EAS Client from the [developer portal](https://portal.easx.ch/) and run: `EASClient.exe --generatekeys eas --keysize 4096`
- Before you can use your subscription to make calls to EASX, we will need to verify and configure it. There are two options to complete your registration:
    1. Run your client locally using `EASClient --host` and navigate to [http://localhost:5000/register](http://localhost:5000/register) page. Input all required data and submit your registration using the UI;
    2. Send an email to [support@easx.ch](mailto:support@easx.ch) with the following infos:
        - username or email you used to sign up for a developer account
        - UIDs ([Unternehmens-Identifikationsnummer](https://www.bfs.admin.ch/bfs/de/home/register/unternehmensregister/unternehmens-identifikationsnummer.html)) of the companies (participants) you need access for
        - the public - _not private_ - key file (.pem) you generated in the previous step
- We will verify your request, activate your subscription and get back to you providing a client certificate which you will need for connecting.

# Installing and configuring EAS Client

The EAS Client is available as a standalone executable or as a Docker image.
For Docker usage and configuration, see [EAS Client Docker Documentation](EAS-Client/Docker.md).

The EAS Client is an executable that hosts the EASX and directory API as a REST API locally. It also provides web pages to easily handle all operations. It can be installed anywhere with access to our [API gateway](https://portal.easx.ch/).
Follow these steps to try it out:

- Download the EAS Client from the [developer portal](https://portal.easx.ch/)
- Place the downloaded _EASClient.exe_ in a folder.
- Place the _client certificate file_ you have received from the EASX team in the same folder.
- Place the _private key file (.pem)_ you have generated also in this folder.
- Add a configuration file named `EASClient.settings.json` next to the EASClient.exe in the same folder with the following content:

  ```json
  {
    "ParticipantId": "<UID of default participant>",
    "EasxSubscriptionKey": "<subscription key for EASX>",
    "PrivateKeyPath": "<path to private key file>",
    "CertificatePath": "<path to client certificate file>",
    "CertificatePassword": "<password for client certificate>",
    "HostUrl": "http://localhost:5000",
    "Environment": "test"
  }
  ```

  Replacing the following values:

  - `<UID of default participant>`: The UID for the participant you will be retrieving or sending documents by default with on this EAS Client.
  - `<subscription key for EASX>`: The primary key for your subscription. Retrieve it from your [profile page](https://portal.easx.ch/profile).
  - `<path to private key>`: Path to the private key file (.pem) which you generated previously.
  - `<path to client certificate file>`: Path to the client certificate file which was provided to you by the EASX team.
  - `<password for client certificate>`: Password for the client certificate file configured above. If no password was provided for the certificate leave this empty.

  Example:

  ```json
  {​​​​​​​
    "ParticipantId": "CHE113558341",
    "EasxSubscriptionKey": "7897eb62e25d456e9d37f7c3e10774e1",
    "PrivateKeyPath": "eas-private-key.pem",
    "CertificatePath": "easx-client.cer",
    "CertificatePassword": "",
    "HostUrl": "http://localhost:5000",
    "Environment": "test"
  }​​​​​​​
  ```

- To test all is configured fine, run `EASClient.exe --list-in` on the command line. If this doesn't return any errors you'll know all is fine.
- Now run `EASClient.exe --host` to start the locally configured and hosted EAS API.
- Now all is set to explore:
  - Open [`http://localhost:5000`](http://localhost:5000) in the browser to play around with the UI.
  - Open [`http://localhost:5000/swagger`](http://localhost:5000/swagger) in your browser to try out the API using Swagger UI.

# Test with Echo Service

To try out sending and receiving documents you can use the Echo Service. The Echo Service is a
participant with UID `CHE000000000` that will receive any document you send to it, send back a receipt and resend the same document back to you.

Get the [prepared demo document](https://easxcommonstorage.blob.core.windows.net/demo-assets/echo-demo-fzl-1-6.xml), add the UID for your sender to the XML, send it and wait a few minutes (upto 15) to receive a receipt and an incoming document from the Echo Service.

# Standard work flows

## Exchange of FZL documents

This is how a full document exchange procedure looks like:

![Document exchange sequence](./Document_Exchange_Sequence.png)

### Sending a document

To send a document to another participant use the following flow of calls:

- `/out-documents - POST` : To upload the content and metdata for the document you want to send. This will return a document id.
- `/out-documents/{id} - PUT` : Sends the uploaded document to the receiver as defined in the metadata.

### Retrieving incoming documents

To retrieve incoming documents use the following flow of calls:

- `/in-documents - GET` : To retrieve the ids and metadata of all the pending documents for this participant.
- For each document (id) received:
  - `/in-documents/{id} - GET` : Get the actual document contents for the given document id. The contents are returned as a string in the "document" field.
  - `/in-documents/{id} - DELETE` : Remove the processed document from your incoming documents. This will automatically send a receipt to the sender.

### Checking receipts

To check if documents you have sent have been received by the receiver:

- `/receipts - GET` : To retrieve all the receipts.
- For each receipt (id) processed:
  - `/receipts/{id} - DELETE` : To remove the receipt from your receipts list.

## Matching entries and exits

The usual flow using the matching service looks like:

![Matching Ablauf](./Matching_Ablauf.svg)

### Notifying a leaving insured

To notify of a current insured leaving the pension fund use the following:
- `/exits - POST`

### Notifying an entering insured

To notify of a new insured entering the pension fund use the following:
- `/entries - POST`

### Check matches for your exits

To check for any matching entries for your exits:
- `/matches/exits - GET`: To retrieve all matches for your exits
- For each match (id) that was processed, remove them:
  - `/matches/exits/{id} - DELETE` : To remove the match from the matches list

<br />

# Further Information

- [Configuring EAS Client](EAS-Client/Settings.md)
- [Commands for EAS Client](EAS-Client/Commands.md)
- [Introduction to the APIs](APIs.md)
