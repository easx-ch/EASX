# Standard Integration Process for EASX in Pension Fund Backend Systems

This guide describes the recommended process for integrating EASX into pension fund backend systems and automating document exchange workflows.

## 1. Setup EAS Client

- Install and configure the EAS Client as described in [Getting-Started.md](Getting-Started.md:1).
- Ensure the backend system can call the EAS Client REST API endpoints.

## 2. Periodic Retrieval and Processing of Incoming Documents

- At regular intervals (recommended: every 15 minutes, minimum: 5 minutes, or daily as per business needs):
  - Call `/in-documents` endpoint to retrieve pending incoming documents.
  - For each document:
    - Retrieve using `/in-documents/{id} - GET`, process and store the document in the backend system.
    - Call `/in-documents/{id} - DELETE` to remove the processed document (this sends a receipt to the sender).

## 3. Outgoing Document Transfer

- When an FZL needs to be transferred to another pension fund:
  - Check if the recipient is a participant in EASX and supports receiving (using the Directory API).
  - If yes:
    - Call `/out-documents - POST` to upload the document and metadata.
    - Call `/out-documents/{id} - PUT` to send the document.
    - Mark the document as "sent" in the backend system.

## 4. Receipt Handling

- At regular intervals (same as incoming document processing):
  - Call `/receipts` endpoint to retrieve all received receipts.
  - For each receipt:
    - Update the document transfer status (success, error) in the backend system.
    - Call `/receipts/{id} - DELETE` to remove the handled receipt.

---

For API details, see [`APIs.md`](../../APIs.md).  
For onboarding and EAS Client setup, see [`Getting-Started.md`](../../Getting-Started.md).
