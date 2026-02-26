
The following error codes may occur when sending requests to EASX APIs:

### UnhandledServerException

This error occurs when the server cannot process the request due to an internal error. This may be caused by database issues, incorrect server configurations, or other internal problems.

### InvalidModel

This error occurs when the data model does not match the expected format or contains invalid values. This may be caused by incorrect data sent to the server.

### EntityNotFound

This error occurs when the requested entity cannot be found on the server. This may be caused by an incorrect identifier or the entity being deleted.

### EntityAccessDenied

This error occurs when the user does not have sufficient access rights to perform the requested operation on the entity. This may be caused by your subscription does not have access to this entity.

### DocumentAlreadySent

This error occurs when the document has already been sent and cannot be sent again. This may be caused by attempting to resend a document already processed.

### IdentifierAlreadyExists

This error occurs when an identifier that is supposed to be unique already exists in the system. This may be caused by attempting to create a new document with a duplicate identifier.

### EntityTooLarge

This error occurs when the entity size exceeds the allowed limit. This may be caused by sending data that is too large to be processed.

### EntityAlreadySecured

This error occurs when an attempt is made to secure an entity that is already secured.

### InvalidReceiver

This error occurs when the recipient of the document is not valid. This may be caused by the receiver not being found.

### SenderIdDoesntMatchInDocument

This error occurs when the sender ID in the document does not match the expected sender ID. This can be caused by the model and document having different sender UIDs.

### ReceiverIdDoesntMatchInDocument

This error occurs when the receiver ID in the document does not match the expected receiver ID. This can be caused by the model and document having different receiver UIDs.

### XmlIsntValid

This error occurs when the XML document is not valid according to the expected schema. This may be caused by incorrect XML formatting.

### DocumentStateNotSent

This error occurs when the document is not in the "sent" state and an operation requires it. This may be caused by attempting operations on a document that hasn't been sent.

### DocumentHasIncorrectState

This error occurs when the document is in the wrong state for the required operation. This may be caused by the fact that the document is in the deleted or revoked status.

### DocumentRevokedProcessed

This error occurs when a revoked document has already been processed. This may be caused by attempting to process a document that has been marked as revoked.

### ParticipantUIDMismatch

This error occurs when there is a mismatch in the participant UID. This can be caused by the model and document having different receiver UIDs

### SubscriptionAccessDenied

This error occurs when access to a subscription is denied. This may be caused by the subscription not being found.

### UnsupportedEncryptionType

This error occurs when the encryption type is not supported. This may be caused by using an invalid encryption method.

### InvalidClientCertificate

This error occurs when the client certificate is invalid. This may be caused by an expired or incorrect certificate.

### InvalidHash

This error occurs when the signature of the document is invalid.

### SigningFailed

This error occurs when the signing document fails. This can be due to an invalid private key configured on the EAS Client.

### DecryptionFailed

This error occurs when the decryption document fails. Possibly it was decrypted by the sender with the wrong public key.

### OutdatedClient

This error occurs if the client version is outdated and unsupported. This may be caused by using an older version of the EASX client software.

### InvalidXmlDocument

This error occurs when the XML document is invalid. This may be caused by incorrect XML formatting or structure.

### XmlMigrationFailed

This error occurs when the XML document migration fails. This may be caused by issues with the migration process, or structure.

### UnsupportedDocumentVersion

This error occurs when the document version is not supported. This may be caused by using an outdated or incorrect document version.

### DocumentCacheIsNotSupported

This error occurs when document caching is not supported. This may be caused by filtering records by xPath when local cache is disabled.

### XmlValidationFailed

This error occurs when the XML validation fails. This may be caused by incorrect XML content or schema.

### PdfRenderingFailed

This error occurs when the PDF rendering fails. This may be caused by issues with the rendering process or incorrect document data.

### ServerMaintenance

This error occurs when the server is undergoing maintenance. This may be caused by scheduled maintenance activities.

### DirectoryServiceIsUnavailable

This error occurs when the directory service is unavailable. This may be caused by authorization issues.

### SenderDoesntHaveAccessToSend

This error may occur if the sender does not have the right to send the document to the recipient. 

### ReceiverDoesntHaveAccessToReceive

This error can occur if the recipient does not have the right to receive the document.


### InvalidTransparencyLogEntry

This error occurs when the TransparencyLog entry is invalid. This may be caused by incorrect data, a corrupted entry, or a mismatch between the expected and actual values in the transparency log.


### TransparencyLogEntryIsMissing

This error occurs when the TransparencyLog entry for the given participant or record cannot be found.