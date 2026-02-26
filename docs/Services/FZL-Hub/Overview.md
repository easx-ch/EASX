# Introduction

The FZL Hub is a service that allows occupational benefits and vested benefits institutions to exchange affiliation data of insured persons. It uses the standardized XML Schema format defined by [BVG Exchange Transfer](https://aeis.ch/en/bvg-exchange/concept#spezifikationen-transfer_E).

# Workflow

The full document exchange procedure is as follows:

![Document exchange sequence](./../../Document_Exchange_Sequence.png)

### Sending Documents

Whenever a participant needs to send the affiliation data of an insured person to another participant, they need to prepare the data as an XML conforming to the FZL XML Schema format and send it to the FZL Hub. The FZL Hub will then forward the document to the recipient. To send a document, use the following flow of API calls:

- `/out-documents - POST`: To upload the content and metadata of the document you want to send. This will return a document ID.
- `/out-documents/{id} - PUT`: Sends the uploaded document to the receiver as defined in the metadata.

### Checking Receipts

To check if the documents you have sent have been received by the recipient:

- `/receipts - GET`: Retrieve all available receipts.
- For each receipt (ID) processed:
  - `/receipts/{id} - DELETE`: Remove the receipt from your list.

### Retrieving Incoming Documents

When utilizing the EAS Client to connect to EASX, there are two options for retrieving incoming documents:

- Processing documents as they arrive
- Searching and processing documents when a payment is received

#### Processing Documents as They Arrive

At regular intervals, receiving participants should retrieve, process, and remove documents with affiliation data. To retrieve incoming documents, use the following flow of API calls:

- `/in-documents - GET`: Retrieve the IDs and metadata of all pending documents for this participant.
- For each document (ID) received:
  - `/in-documents/{id} - GET`: Get the actual document contents for the given document ID. The contents are returned as a string in the "document" field.
  - `/in-documents/{id} - DELETE`: Remove the processed document from your incoming documents. This will automatically send a receipt to the sender.

#### Searching and Processing Documents When a Payment is Received

When a payment or another event that requires processing of received data occurs, you can search for and process the relevant documents using the following steps:

- `/in-documents - GET`: Use XPath filtering to search for relevant documents. For details on using XPath filtering, see [Filtering using XPath](../../EAS-Client/Filter-Using-XPath.md). This will return the IDs and metadata of all relevant documents.
- For each relevant document (ID) found:
  - `/in-documents/{id} - GET`: Retrieve the document contents. The contents are returned as a string in the "document" field.
  - `/in-documents/{id} - DELETE`: Remove the processed document from your incoming documents. This will automatically send a receipt to the sender.

Note: To use XPath filtering the EAS Client must be correctly configured as explained in [Filtering using XPath](../../EAS-Client/Filter-Using-XPath.md) Configuration section.

# Suggested Integration

For a standard process of integrating into the pension fund backend system check out [Standard Integration Process](Standard-Integration-Process.md).
