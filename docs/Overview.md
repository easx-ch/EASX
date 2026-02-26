# Introduction 

EASX is a secure platform providing services for the digital connection of Swiss pension funds.

The following services are currently provided:
- *Exchange of insurer values* - Any pension fund can easily connect to the EASX REST APIs to send and receive the insurer values from or to any other connected pension fund.
- *Matching entries to exits* - This service allows the automatic detection and notification of matching exits and entries of insured of pension funds. This allows pension funds to proactively initiate the transfer of any leaving insureds values to a new pension fund.
- *WAK notifications* - This service allows pension funds to send the required Reinstatement Notification (WAK = Wiederanschlusskontrolle) to the Substitute Occupational Benefit Institution LOB (AEIS = Stiftung Auffangeinrichtung BVG) when an employer leaves a pension fund.

Learn more about these in [Services](./Services/Overview.md).

# Architecture

EASX consists of two main components: EAS Client and the EASX Server.

![User Architecture Diagram](./User_Architecture_v0.2_cropped.png)

The EAS Client is installed by the participant on their servers or cloud as a binary executable or a [docker container](https://hub.docker.com/r/easx/client).
For detailed Docker usage and configuration, see [EAS Client Docker Documentation](EAS-Client/Docker.md).
Once configured the pension fund system can access the EAS Client API for all EASX operations. The EAS Client enables
a full end-to-end encryption which ensures highest level of security. It also handles validation, interoperability for
different versions of data and the communication with the EASX Server.

The EASX Server provides the services through an API Gateway accessible on https://api.easx.ch. It is secured using SSL, client certificates and subscription keys.
All sensitive data is transferred to the EASX services using secure PK encryption, with participant public keys tracked and verified via [Transparency Logs](./Services/Directory/Transparency-Logs.md), providing the highest level of trust and data protection for the participants.

## APIs

For accessing EASX from a pension fund system multiple REST APIs are provided: Hub API, Directory API, Matching API and WAK API.

You can find more information in the [introduction to the APIs](APIs.md).

# Getting Started

To try out and get up and running checkout the [Getting Started](Getting-Started.md) page.

# Resources

- *Portal* - [https://portal.easx.ch](https://portal.easx.ch) - main entry point and registration
- *Documentation Test Environment* - [https://docs-test.easx.ch](https://docs-test.easx.ch) - Documentation for the version running in the *Test* environment
- *Documentation Production Environment* - [https://docs.easx.ch](https://docs.easx.ch) - Documentation for the version running in the *Production* environment
- *EASX API* - [https://api.easx.ch/api](https://api.easx.ch/api) - Root for all APIs on the EASX Server
- *EAS Client Docker* - [https://hub.docker.com/r/easx/client](https://hub.docker.com/r/easx/client) - EAS Client docker image on Docker Hub ([see Docker documentation](EAS-Client/Docker.md))


---

Contact [support@easx.ch](mailto:support@easx.ch) with any questions or issues.
