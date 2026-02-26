# Transparency Logs Page (UI Usage)

The Transparency Logs Page in the EAS Client GUI provides users with a comprehensive view of transparency logs, supporting auditability and verification of key events and actions. This page is designed to help users audit (view, verify, and export) logs related to the public keys used for end-to-end encryption to other participants.

> **Important Note:**  
> The first time the full audit log is retrieved from the server, loading and display may take several minutes. Subsequent loads will be faster due to cached data. However, because of caching, the displayed data may be up to 30 minutes old and thus not absolutely current.

For conceptual details, see [Transparency Logs Mechanism](../Services/Directory/Transparency-Logs.md).

## Tabs Overview

### Logged Public Keys

Shows all logged public keys and verification information of participants you have sent messages to.

### Audit Log

Lists all entries in the Rekor transparency log. This tab enables users to analyze the full chain of transparency log events, inspect log entries, filter by participant, and download logs (using Export to JSON button) for further analysis.

### Verification

Compares logged public keys to transparency log entries to audit that the keys used are actually present in the transparency log. Users can run Rekor chain verification to ensure logs have not been tampered with. Feedback is displayed indicating verification success or highlighting any detected issues.

## Participant Selection and Filtering

Users can select or filter participants to focus on specific log entries. Filtering is especially useful to narrow down relevant entries, such as when checking if the known history of your own public keys has been untampered in the transparency log. Filtering affects which logs are displayed in the Rekor and Verification tabs, enabling targeted audits and streamlined analysis.

## Downloading Transparency Logs

Transparency logs can be downloaded for audit or export purposes. Use the `Export to JSON` button on any tab to export logs in a standard format for external review or archival. The exported data is dependent on the tab and participant filter you have selected.

## Transparency Log Chain Verification

The "Verify Chain of Transparency Logs" button performs a check of the full transparency log chain. It works the same regardless of which tab is open. When executed, the system checks for tampering or inconsistencies across the entire log. Feedback is provided:

- **Success:** Logs are intact and untampered.
- **Failure:** Issues are highlighted, indicating possible tampering or missing entries.

## Practical Usage Notes

- Use the transparency log chain verification to make sure the full transaction log is untampered.
- Use participant filtering to narrow down relevant entries, especially for verifying the untampered history of your own public keys in the transparency log.
- Use the Verification tab to make sure the logged publickeys match the transparency log entries.
- Download the full transparency logs for independent verification.
- If verification fails, investigate discrepancies immediately.

---

**More information:**
See [Transparency Logs Mechanism](../Services/Directory/Transparency-Logs.md) for a deeper explanation of transparency logs and their role in EASX.
