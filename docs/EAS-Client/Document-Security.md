# Document Security

The EAS Client handles document signing and encryption automatically. Applications using the local API or command-line commands should provide the document as plain XML and should not create `EncryptionProps` or signatures themselves.

## Automatic negotiation

The client reads the security capabilities of the sender and receiver from the Directory Service. It uses `GcmPssSha256` only when both participants support it and the receiver's public RSA key is compatible with GCM. In all other cases it uses the backward-compatible `Legacy` level.

| Level | Encryption | Signature |
|---|---|---|
| `Legacy` (`0`) | `MetaPK`: AES-CBC with RSA-OAEP-SHA1 key wrapping | SHA-1 with RSA PKCS#1 v1.5 |
| `GcmPssSha256` (`1`) | `MetaPK-GCM`: AES-256-GCM with RSA-OAEP-SHA256 key wrapping | SHA-256 with RSA-PSS |

The table assumes that the receiver has a public key. If no public key is configured, the payload is sent with `EncryptionType=None`. If a public key exists, it must be at least 2048 bits for `MetaPK-GCM`; a smaller key causes automatic fallback to `MetaPK`.

## What the API returns

After the client receives a document, it decrypts and verifies it before returning it to the local application. The application normally sees the original XML. The transport fields have these meanings:

- `EncryptionType` identifies the encryption format (`None`, `MetaPK`, or `MetaPK-GCM`).
- `EncryptionProps` contains encrypted metadata required to decrypt the payload.
- `Signature` contains the document signature.

Modern signatures start with `PSS-SHA256:`. Signatures without this prefix use the legacy SHA-1 format. The signature is calculated over the original UTF-8 XML before encryption.

Receipts are encrypted when the receiver has a public key, but are not signed. WAK notifications use the negotiated encryption and signature level, or `EncryptionType=None` when the receiver has no public key.
