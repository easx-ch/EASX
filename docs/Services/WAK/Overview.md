# Introduction

When an employer leaves a pension fund a Reinstatement Notification (WAK = Wiederanschlusskontrolle) has to
be sent to the Substitute Occupational Benefit Institution LOB (AEIS = Stiftung Auffangeinrichtung BVG).

EASX provides a service for registered participants to send the required data to AEIS.

Participants can use the WAK Service independently of other used services, allowing them to choose 
which EASX services to use and to what extent.

# Workflow

To send a WAK notification use the following flow of calls:

- `/notifications - POST` : To upload the notification data you want to send. This will return a notification id.
- `/notifications/{id} - PUT` : Sends the uploaded notification data to the AEIS.

You can check if notifications have been received (successfully or with errors) using the following call:

- `/receipts - GET` : Returns a list of all notifications handled by the receipts and if successful or any errors occured.

Remove receipts after processing so they don't appear anymore using the following call:

- `/receipts/{recId} - DELETE` : Removes the receipt with the given id.

# Document

The document to pass to `/notifications - POST` is an XML conforming to the WAK specification from [BVG exchange](https://aeis.ch/bvg-exchange/konzept#spezifikationen-transfer)