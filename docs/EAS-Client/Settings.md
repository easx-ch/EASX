This document explains where to configure EAS Client settings and contains detailed descriptions of all parameters that can be configured in EASX Client.

## How to configure

There are 3 ways of configuring the EAS Client.

### A. Command line parameters

Pass a value when launching the app. Example:

`EASClient.exe --ParticipantId CHE123456789 --EasxSubscriptionKey 123456789abcd`

Make sure you use quotes in case parameter values contain whitespaces. Example:

`EASClient.exe --PrivateKeyPath "C:\keys\file name with whitespaces.pem"`

### B. Settings json file

First of all, create a `*.settings.json` file in the same folder EAS Client executable is located. By default, client executable is called, `EASCLient.exe`, so the file should be named `EASClient.settings.json`.

Next, just place parameters into that file. Example:

```json
{
  "ParticipantId": "CHE123456789",
  "EasxSubscriptionKey": "123456789abcd"
}
```

### C. Environment variables

Environment variables can also be used to configure the app. This way of configuring EAS Client may be useful if you're planning to use containers.


### Combination of configuration approaches

You can use any combination of the configuration approaches above. 
E.g. you can specify some of the values in settings file and pass the others via the command line.

In case the same setting is encountered both in the settings file and in command line, only the command line parameter will be taken into account.
The priority of environment variables are higher than settings json, but lower than command line arguments.

## Parameters list

This is the list of all available parameters. In case a parameter is marked as required, EAS Client will not start without it. Though some parameters are not required (e.g. `PrivateKeyPath`), you may still need to specify them, based on the way your participant is configured on the server side.
All paths can be relative, absolute, or in any other format as long as it's supported by the operating system.

| Name                    | Default               | Example                | Required | Description                                                                                                                                           |
| ----------------------- | --------------------- | ---------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| ParticipantId           | null                  | CHE123456789           | Yes      | Enterprise Identification Number (UID) of the participant. It should not include whitespaces, punctuation marks or any extra characters.              |
| EasxSubscriptionKey     | null                  | 123abc345def78d2       | Yes      | Your Subscription Key. The one for testing can be generated in EASX Developer Portal.                                                                 |
| Endpoint                | https://api.easx.ch   |                        | No       | Web URL of EASX Server API. Usually, there is no reason to change it, unless you are using a proxy or some kind of a firewall.                        |
| PrivateKeyPath          | null                  | private_key.pem        | No       | A path to your private key file. After it is configured on the EASX Server side, it will be used to decrypt and sign messages.                        |
| PrivateKeyContent       | null                  | base64string           | No       |This param is used for Docker Container. You should provide it as reference to Key Vault in Azure|
| AltPrivateKeyPath          | null                  | alt_private_key.pem        | No       | A path to your alternate private key file. After a new one key is configured on the EASX Server side, it will be used to decrypt messages, which were sign by old key.                        |
| AltPrivateKeyContent       | null                  | base64string           | No       |This param is used for Docker Container. You should provide it as reference to Key Vault in Azure|
| CertificatePath         | null                  | `C:/eas/certificate.pfx` or `store://CurrentUser/My/fe44b4c2b44...` | No | A path to your client certificate file. If it is configured on the EASX Server side, it's thumbprint will be used to validate requests. Alternatively, you can specify a certificate stored in your Operating System by using the following format: "store://[StoreLocation](https://docs.microsoft.com/en-us/dotnet/api/system.security.cryptography.x509certificates.storelocation?view=net-5.0)/[StoreName](https://docs.microsoft.com/en-us/dotnet/api/system.security.cryptography.x509certificates.storename?view=net-5.0)/thumbprint"|
| CertificateContent      | null                  | base64string           | No       | This param is used for Docker Container. You should provide it as reference to Key Vault in Azure|
| CertificatePassword     | null                  | qwerty123!             | No       | If the pfx file with a client certificate is password protected, specify it here. Otherwise, leave this field as null.                                |
| HostUrl                 | http://localhost:5000 | http://localhost:5050  | No       | A URL where client GUI and Swagger should be located if the client was launched in a host mode. It can be any valid URL.                              |
| Environment             | test                  |                        | No       | Environment that is used by the EAS Client. Set to "test" for testing or "prod" for production environments.                                          |
| ProxyHost               | null                  | http://proxy.local     | No       | Proxy host address in case your system requires proxy to access internet.                                                                             |
| ProxyPort               | null                  | 4444                   | No       | The port your proxy host is running on.                                                                                                               |
| ProxyUsername           | null                  |                        | No       | The username for the configured proxy.                                                                                                                |
| ProxyPassword           | null                  |                        | No       | The password for the configured proxy.                                                                                                                |
| SecurityProtocol        | SystemDefault         | Tls12                  | No       | [Supported values.](https://docs.microsoft.com/en-us/dotnet/api/system.net.securityprotocoltype) Specifies the security protocol that should be used. |
| Expect100Continue       | true                  |                        | No       | Specifies if 100-Continue behavior is enabled. Can be useful in advanced proxy configuration.                                                         |
| Http2Support            | true                  |                        | No       | Specifies if HTTP2 should be enabled. Can be useful in advanced proxy configuration.                                                                  |
| Http2UnencryptedSupport | false                 |                        | No       | Specifies if HTTP2 can be used without encryption. Can be useful in advanced proxy configuration.                                                     |
| OverrideParticipant     | false                 | ```{ "CHE_MULTIPLE_5": { "PrivateKeyPath": "CHE_MULTIPLE_5-private_key.pem", "CertificatePath": "CHE_MULTIPLE_5-client_certificate (1).p12", "EasxSubscriptionKey": "0a9f40f2e285490d8e1ccd3f2fd412da"}}  ```                   | No       | Configure different keys, certificates or subscriptions for accessible participants|
| DocumentCacheMode       | Disabled              |                        | No       | The document cache mode. Possible values: <ul><li>'Disabled' - The cache is not working</li><li>'EnabledWithoutPrefetch' - The cache working without a job in parallel mode</li><li>'Enabled' - the cache is working</li><ul>     
| SyncDocumentsIntervalMinutes | 5                |                        | No       | The cache document task execution interval in minutes    
| TransparencyLogsCacheTimeout | 1800             |                        | No       | Specifies the cache expiration time (in seconds) for transparency log entries. Default is 1800 seconds
| TransparencyLogsLocalFileName | publicKeyStorage.json                 |  | No       | Specifies the name of the local file used to store transparency log records (e.g. public keys).    
| TransparencyLogsVerificationIsEnabled | true    |                        | No       | Indicates whether verification of entries against the transparency log is enabled    
| TransparencyLogsStoreParticipantIsDisabled | false  |                    | No       | Indicates whether storing all received user public keys into the local JSON file is disabled
| TransparencyLogsBatchSize | 5                   |                        | No       | Defines the number of records retrieved from the Directory Service in a single request    
| TransparencyLogsMaxConcurrency | 30                 |                    | No       | Specifies the maximum number of requests to the Directory Service that can be executed in parallel    
| CachePath | .cache                 |                    | No       |Path to the folder where all cached documents are stored. For Docker containers, it is not recommended to change this path since it is persisted in the `/Data` volume.   
| LoggedKeysPath | LoggedKeys                 |                    | No       | Path to the folder where the JSON file with retrieved public keys is stored. For Docker containers, it is not recommended to change this path since it is persisted in the `/Data` volume.   
| LogsPath | Logs                 |                    | No       | Path to the folder where application logs are stored. For Docker containers, be cautious when changing this path, as logs are persisted in the `/Logs` volume.   


**Advanced logging configuration**

There are 2 optional configuration sections for logging. `SerilogCLI` section is being used in case EAS Client was launched in command line mode. `SerilogHost` takes effect in host mode. In case a configuration section is specified, `--debug` option will not take effect.
Both of them are [logger configuration sections](https://github.com/serilog/serilog/wiki/Configuration-Basics) in json [format](https://github.com/serilog/serilog-settings-configuration). Log configuration can be used to change log level, add or remove additional logging targets (e.g. log exceptions to a separate file), change format of logged messages, modify colors (e.g. print warnings in red), etc.

You can find the defaults below:

```json
"SerilogCLI": {
  "MinimumLevel": {
    "Default": "Warning",
    "Override": {
      "System": "Warning",
      "Microsoft": "Warning"
    }
  },
  "WriteTo": [
    {
      "Name": "Console",
      "Args": {
        "theme": "Serilog.Sinks.SystemConsole.Themes.AnsiConsoleTheme::Code, Serilog.Sinks.Console",
        "restrictedToMinimumLevel": "Warning"
      }
    },
    {
      "Name": "File",
      "Args": {
        "path": "Logs/log.txt",
        "rollingInterval": "Day"
      }
    }
  ],
  "Enrich": [ "FromLogContext" ]
},
"SerilogHost": {
  "MinimumLevel": {
    "Default": "Warning",
    "Override": {
      "System": "Warning",
      "Microsoft": "Warning"
    }
  },
  "WriteTo": [
    {
      "Name": "Console",
      "Args": {
        "theme": "Serilog.Sinks.SystemConsole.Themes.AnsiConsoleTheme::Code, Serilog.Sinks.Console"
      }
    },
    {
      "Name": "File",
      "Args": {
        "path": "Logs/log.txt",
        "rollingInterval": "Day"
      }
    }
  ],
  "Enrich": [ "FromLogContext" ]
}
```

If you run EAS Client with `--debug` enabled, following configurations will be used instead:

```json
"SerilogCLI": {
  "MinimumLevel": {
    "Default": "Verbose",
    "Override": {
      "System": "Verbose",
      "Microsoft": "Verbose"
    }
  },
  "WriteTo": [
    { "Name": "Debug" },
    {
      "Name": "Console",
      "Args": {
        "theme": "Serilog.Sinks.SystemConsole.Themes.AnsiConsoleTheme::Code, Serilog.Sinks.Console",
        "restrictedToMinimumLevel": "Warning"
      }
    },
    {
      "Name": "File",
      "Args": {
        "path": "Logs/log.txt",
        "rollingInterval": "Day"
      }
    }
  ],
  "Enrich": [ "FromLogContext" ]
},
"SerilogHost": {
  "MinimumLevel": {
    "Default": "Verbose",
    "Override": {
      "System": "Verbose",
      "Microsoft": "Verbose"
    }
  },
  "WriteTo": [
    { "Name": "Debug" },
    {
      "Name": "Console",
      "Args": {
        "theme": "Serilog.Sinks.SystemConsole.Themes.AnsiConsoleTheme::Code, Serilog.Sinks.Console"
      }
    },
    {
      "Name": "File",
      "Args": {
        "path": "Logs/log.txt",
        "rollingInterval": "Day"
      }
    }
  ],
  "Enrich": [ "FromLogContext" ]
}
```
