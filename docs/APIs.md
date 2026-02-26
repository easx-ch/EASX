APIs provide all the operations a pension fund system needs to access the EASX services:

# EASX Hub API

The actual REST API providing all the features needed to send and receive insurer values (documents).

It contains the following resources:
- `in-documents`: Handles the FZL data (pension transfer documents) that the caller has received.
- `out-documents`: Allows the caller to send FZL data (pension transfer documents) to other participants.
- `receipts`: Provides handling of receipts received for documents the caller previously sent. 
- `logs`: Provides logging information relevant to the caller.

For detailed documentation of the available operations check out the [Hub API details](https://portal.easx.ch/api-details#api=60d2f0460d4f28337a74fca8) (signin required) on the EASX Portal.

# EASX Directory API

This REST API allows retrieving the information on all participants reachable using EASX.

It contains the following resources:
- `participants`: Provides information on all participants in the EASX system.
- `me`: Provides information about the caller.

For detailed documentation of the available operations check out the [Directory API details](https://portal.easx.ch/api-details#api=60d2f0fa6fb64e25dfd12323) (signin required) on the EASX Portal.

# EASX Matching API

The REST API for notifying on leaving or entering insured and retrieving any matching transfers.

It contains the following resources:
- `exits`: Handles the notification of any insureds leaving a current pension fund.
- `entries`: Handles the notification of any insureds entering a new pension fund.
- `matches/exits`: Provides matches for any exits to appropriate entries.
- `matches/entries`: Provides matches for any entries to appropriate exits.
- `logs`: Provides logging information relevant to the caller.

For detailed documentation of the available operations check out the [Matching API details](https://portal.easx.ch/api-details#api=65a181aa684688d98704bc6f) (signin required) on the EASX Portal.

# EASX WAK API

The REST API for sending Reinstatement Notification (WAK = Wiederanschlusskontrolle) to the Substitute Occupational Benefit Institution LOB (AEIS = Stiftung Auffangeinrichtung BVG) when an employer leaves a pension fund.

It contains the following resources:

- `notifications` : Allows sending the Reinstatment (WAK) notifications to AEIS..
- `receipts` : Provides receipts for checking if notifications have been received (successfully or with errors).
- `logs`: Provides logging information relevant to the caller.

For detailed documentation of the available operations check out the [WAK API details](https://portal.easx.ch/api-details#api=663ca6ace61759246f0a3442) (signin required) on the EASX Portal.
