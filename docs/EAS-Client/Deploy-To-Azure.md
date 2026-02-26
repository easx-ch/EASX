The following instructions show how to install the EAS Client as an Azure App Service and 
using Azure Key Vault to secure the sensitive configuration settings.

# Prerequisite
1. You should have an Azure Account.
2. You should have a Key Vault resource in your Azure cloud.
3. You should have registered a subscription for an EASX participant and have all EAS configurations available (subscription key, private key, certificate).

# Option A (Recommended): App Service Creation from Docker Hub
This is the default and recommended option.

No Azure Container Registry is required.

1. Open next link https://portal.azure.com/#create/Microsoft.WebSite.
2. Input your data to all required fields.
    - Check `Docker Container` for `Publish` option;
    - Check `Linux` for `Operating System` option;
3. Go to next step;
    - Select `Single Container` for `Options` option;
    - Select `Docker Hub` for `Image Source` option;
    - Select `Public` for `Access Type` option;
    - Input `eas/client:version for `Image and Tag` option;
4. Finish configure your application and create a new Web App Service.

# Option B (Alternate): App Service Creation from Azure Registry
This option is intended for advanced scenarios where you already manage your own Azure Container Registry.

**Important notes:**
- An Azure Container Registry must already exist before starting.
- The documentation assumes:
  - A registry named `eashub`
  - An image named `client1`
- If your registry or image names differ, replace them accordingly.

**Steps:**
1. Open next link https://portal.azure.com/#create/Microsoft.WebSite.
2. Input your data to all required fields.
    - Check `Docker Container` for `Publish` option;
    - Check `Linux` for `Operating System` option;
3. Go to next step;
    - Select `Single Container` for `Options` option;
    - Select `Azure Container Registry` for `Image Source` option;
    - Select `eashub` for `Registry` option;
    - Select `client1` for `Image` option;
    - Select last version for `Tag` option;
4. Finish configure your application and create a new Web App Service.

# Identity creating and Key-Vault binding
1. Open the application you created in the previous step.
2. Open the `Settings>Identity` tab on the left sidebar.
3. Swith status to `on` and save your changes.
4. Go to your key vault resource.
5. Open the `Settings>Access policies` tab on the left sidebar.
6. Click on `+ Add Access Policy`
7. Configure the following fields:
    - Select `Get` for `Secret Permissions` option;
    - Select your application for `Select Principal`;
8. Click on `Add` button and save all changes.

# Configure settings for application
1. We recommend to store all your sensitive data in the KEY VAULT.
2. Open  your key vault resource.
3. Open a `Settings>Secrets` tab on the left sidebar.
4. Click on `+ Generate/Import` and create next secrets:
    - Name `EasxSubscriptionKey` and provide your key as a value;
    - [NOT REQUIRED] Name `Environment` and provide your environment as a value;
    - [NOT REQUIRED] Name `ParticipantId` and provide your participantId as a value;
5. Click on `+ Generate/Import` and upload your private key and certificate:
    - Select `Certificate` for `Upload options` field;
    - Set a name `Certificate`;
    - Select a certificate from you local files;
    - Do the same steps for your private-key;
6. Open and application, which you create.
7. Open a `Settings>Configuration` tab on the left sidebar.
8. For example, a complete reference would look like the following:
```@Microsoft.KeyVault(SecretUri=https://myvault.vault.azure.net/secrets/mysecret/)```
  
   Alternatively:
`@Microsoft.KeyVault(VaultName=myvault;SecretName=mysecret)`

9. You should add next properties:

    - `CertificateContent` should be bind to Key Vault;
    - `PrivateKeyContent` should be bind to Key Vault;
    - `EasxSubscriptionKey` should be bind to Key Vault;
    - `Environment` you can bind it to Key Vault or if you don't define it, you can provide it as a string;
    - `ParticipantId` you can bind it to Key Vault or if you don't define it, you can provide it as a string;