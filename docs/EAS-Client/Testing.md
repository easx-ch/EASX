# Testing

Test Mode lets you exercise the EAS Client API from your own application or the Web UI — without sending real documents, creating real participants, or reaching the real API. Every response is simulated locally by the client; no network call leaves the machine.

Use it to verify your integration's request/response handling against the API without risking real data or needing a second subscription.

**What it does not test:** since no call reaches the real API, Test Mode doesn't verify your certificate/subscription-key setup or that a document is actually delivered to another participant. For a real, full round-trip test, use the [Echo Service](../Getting-Started.md#test-with-echo-service) instead.

## Enabling Test Mode

Send a `test-mode` header with your API requests:

```sh
curl http://localhost:5000/api/directory/v1/me/participants -H "test-mode: Mocked"
```

| Header value               | Behaviour                                                                       |
| -------------------------- | ------------------------------------------------------------------------------- |
| _(omitted)_ / `Disabled`   | Normal operation. All data is real.                                             |
| `MockedExceptParticipants` | All responses simulated, except participant lookups, which use real identities. |
| `Mocked`                   | Fully simulated, including participants.                                        |

### Web UI

The **Testing** page sets the same header for you. Pick a mode there instead of setting headers manually. Changes take effect on the next page load or navigation.

## Mocked Participants

`Mocked` mode returns two built-in sample participants, generated automatically at startup:

| UID            | Name          |
| -------------- | ------------- |
| `CHE999000001` | Participant A |
| `CHE999000002` | Participant B |

Use these UIDs as sender/receiver when testing document flows.

## Resetting Mocked Data

The **Reset Mocked Data** button on the Testing page clears simulated state accumulated during testing, without touching your real configuration or credentials.
