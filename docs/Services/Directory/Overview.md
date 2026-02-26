The Directory Service provides information on all participants accessible using EASX and configuration information.

One use case for accessing the Directory Service are to verify whether a pension fund is a participant that can send or receive data on EASX.
This can be accomplished using the following API calls:
- `/participants - GET`: Retrieves a list of all participant UIDs and names in the EASX system.
- `/participants/{participantUid} - GET`: Returns details of a specific participant, including whether the participant can send or receive FZL documents.
- 
The directory service also contains endpoints for retrieving the public key(s) of a participant and accessing the entries of the [transparency log](Transparency-Logs.md).

For detailed documentation on available operations, visit the [Directory API details](https://portal.easx.ch/api-details#api=60d2f0fa6fb64e25dfd12323) (signin required) on the EASX Portal.
