# Introduction

When an employee in Switzerland changes jobs, the pension fund (PF) of the previous employer
is legally required to transfer the entire vested benefits (FZL) to the pension fund of the new employer.

Before the introduction of the Matching Service, pension funds depended on the departing beneficiary to 
provide all necessary details for transferring their vested benefits, including the name, address,
and account of the new pension fund. This process involved considerable manual effort for both pension 
funds and beneficiaries.

The Matching Service simplifies this process by automatically mapping entries to appropriate exits and
notifying the involved pension funds. As a result, the pension fund from which a beneficiary departs can
receive all the details needed to transfer the vested benefits (FZL) to a new pension fund automatically
and digitally.

The actions taken by the participating pension funds upon notification of a match are determined 
individually and remain under the full control of the participant. This could include transferring 
the vested benefits automatically or requesting confirmation from the beneficiary before proceeding with 
the transfer.

Participants can use the Matching Service independently of the FZL Hub Service, allowing them to choose 
which EASX services to use and to what extent.

# Workflow

All participating pension funds notify the Matching Service API of any beneficiary exits and entries.

Note: Make sure to remove the existing entry for this exit to avoid receiving an unnecessary match from 
the own entry.

Participants should check the matches they have received for their notified exits at regular intervals and 
initiate the appropriate actions in their systems. The interval at which they check the system for matches
is up to the participant, usually every few minutes or hours.

# Matching logic

Whenever any new exit or entry is added, the service checks for any matching entries or exits. These
matches are then added to the appropriate participant's list of matches for exits and, if requested when 
adding the entry, to the list of matches for entries. 

Note: Although the system usually adds matches immediately on notifying of an entry or exit. The matches
can also be added by the system asynchronously, so a participant should not rely on matches being avaialble
immediately after adding an entry or exit.

# Securing personal data

To protect personal data from being accessed by unauthorized participants, only a hash identifying a 
beneficiary by their social security number and birthdate is used. This hash is generated using a one-way
hashing algorithm, ensuring that the personal data represented by the hash cannot be deduced. The algorithm
used is described in more detail in [personal hash](Personal-Hash.md).
