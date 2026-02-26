# Transparency Logs Mechanism

## Overview

Transparency logs are a core security feature of the EASX platform, designed to provide verifiable, tamper-evident records of participant public keys. By leveraging transparency logs, EASX ensures that all participant public keys (primary and alternate) are publicly auditable, which is essential for maintaining trust and enabling secure end-to-end encryption.
EASX implements transparency logs using [Rekor](https://docs.sigstore.dev/logging/overview/), an open-source transparency log system.

## What Are Transparency Logs?

A transparency log is an append-only, cryptographically verifiable ledger. Each entry in the log records a participant's public key (primary and, if present, alternate), and is signed and timestamped. The log is structured as a Merkle tree, allowing anyone to verify the inclusion and integrity of entries without exposing sensitive data.

## How Transparency Logs Secure End-to-End Encryption

- **Key Registration:**  
  When a participant joins EASX or updates their cryptographic keys, a signed entry is added to the transparency log. This entry includes the participant's unique identifier (UID), primary public key, and (if applicable) alternate public key.

- **Public Auditability:**  
  Anyone can verify that a participant's public key is registered and has not been tampered with by checking the log entry and its cryptographic proof. This prevents unauthorized key changes and enables trust towards the provider of the EASX platform.

- **Tamper-Evidence:**  
  The log uses Merkle tree proofs and digital signatures to ensure that any attempt to modify or remove entries is detectable. This guarantees the integrity of the key material used for encryption.

- **End-to-End Encryption:**  
  Before sending encrypted data, the sender verifies the recipient’s public key against the transparency log. This ensures that only the intended recipient, whose key is verifiably registered, can decrypt the data.

## Typical Workflow

1. **Participant Key Registration:**  
   - The participant submits their public key to EASX.
   - EASX creates a signed transparency log entry for the key.

2. **Verification Before Encryption:**  
   - The sender retrieves the recipient’s public key from the Directory Service.
   - The sender verifies the key’s transparency log entry and inclusion proof.

3. **Secure Data Exchange:**  
   - Data is encrypted using the verified public key.
   - The recipient can decrypt the data, confident that the key is authentic and untampered.

## API Integration

- The Directory Service exposes endpoints to retrieve participant public keys and associated transparency log entries.
- Each participant’s details include their current public key(s) and the corresponding transparency log proofs.

## Benefits

- **Trust:** All participants can independently verify key authenticity.
- **Security:** Prevents man-in-the-middle attacks and unauthorized key changes.
- **Auditability:** Enables external audits and compliance checks.

## Further Reading

- [Directory Service Overview](./Overview.md)
- [EASX API Documentation](https://portal.easx.ch/api-details#api=60d2f0fa6fb64e25dfd12323) (signin required)

