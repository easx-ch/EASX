First of all, to connect to EASX you will need to have an appropriate developer account and product subscription. Refer to the [Getting Started](Getting-Started.md) for more details.

There are multiple options of connecting to EAS.

![User Architecture Diagram](./User_Architecture_v0.1_cropped.png)

**NOTE**: In most cases the 2. option (using EAS Client) is the best approach.

## 1. Connecting directly to the EAS service

This approach is the easiest and quickest to get up and running, but does not provide maximum end-to-end security. It requires you to make calls directly to EAS API. You can find specifications, request structure, samples of code in most programming languages on the [Developer Portal](https://portal.easx.ch/).

For example, to get a list of incoming documents using this method, you will have to send a `GET` request to the specific URL and handle resulting response in json format. This can be done in any programming language, or even with a batch script using curl. Thus, it is possible to create a batch/shell script and configure it to run every few hours using Windows Task Scheduler or a cron job.

This method requires you to attach a few security related headers and specify a client certificate file. But, encryption, decryption and signing of the documents is handled on the server side. So, EAS API will expect you to send and receive documents in clear text. All messages will still be encrypted and validated (https, subscription keys, client certificates), but there will be no end to end encryption of the document payload.

## 2. Connecting via the EAS Client

This option is the **prefered option** suggested for almost all cases.

Using this approach a full end-to-end encryption can be utilized, ensuring highest levels of security. It requires an installation of a single-file application
or a docker image, provided by EAS (see [Docker Usage and Configuration](EAS-Client/Docker.md) for details). Updates and improvements of the EAS Client are maintained by us. This is our suggested option, balancing simplicity and security. EAS Client silently handles signing, verification, encryption/decryption and version migrations of documents in your environment.

## 3. Implementing the EAS Client in your application

This approach also provides an end-to-end encryption, ensuring highest levels of security. But it means implementing and maintaining the code, handled by our provided EAS Client, in your application yourself. EAS Client does not use any custom encryptions, so it's highly likely that the programming language you've chosen will already have all required features in form of some library.
In case you'd like to follow this approach, make sure you contact us at [support@easx.ch](mailto:support@easx.ch). We will gladly provide you all details and code samples required to implement EAS Client features correctly.
