## Software requirements

EAS Client is supported on multiple operating systems.

### Windows

| OS                  | Version            | Architectures   |
| ------------------- | ------------------ | --------------- |
| Windows (Legacy)    | 7 SP1(**\***), 8.1 | x64, x86        |
| Windows 10          | Version 1607+      | x64, x86, Arm64 |
| Windows 11          | Version 2200+      | x64, x86, Arm64 |
| Windows Server      | 2012+              | x64, x86        |
| Windows Server Core | 2012+              | x64, x86        |
| Nano Server         | Version 1809+      | x64             |

**\*** Windows 7 SP1 is supported with [Extended Security Updates](https://docs.microsoft.com/troubleshoot/windows-client/windows-7-eos-faq/windows-7-extended-security-updates-faq) installed.

### Linux

| OS                           | Version                    | Architectures     |
| ---------------------------- | -------------------------- | ----------------- |
| Alpine Linux                 | 3.11+                      | x64, Arm64        |
| CentOS                       | 7+                         | x64               |
| Debian                       | 9+                         | x64, Arm32, Arm64 |
| Fedora                       | 33+                        | x64               |
| Linux Mint                   | 18+                        | x64               |
| openSUSE                     | 15+                        | x64               |
| Red Hat Enterprise Linux     | 7+                         | x64               |
| SUSE Enterprise Linux (SLES) | 12 SP2+                    | x64               |
| Ubuntu                       | 21.04, 20.04, 18.04, 16.04 | x64, Arm32, Arm64 |

### macOS

| OS    | Version | Architectures |
| ----- | ------- | ------------- |
| macOS | 10.13+  | x64           |


## Hardware requirements

| Property          | Minimal | Recommended |
| ----------------- | ------- | ----------- |
| CPU Frequency     | 1GHz    | 2GHz        |
| RAM               | 512Mb   | 1Gb         |
| Disk space        | 300Mb   | 512Mb       |
| Network Bandwidth | 64Kb/s  | 256Kb/s     |
| GPU / Display     | none    | none        |

Note: EAS Client can act as a local server, providing access to API and Web GUI. Consequently, expected load must be taken into account when calculating hardware requirements. Minimal values specified in this table will allow the app to work with 1 browser session or concurrently execute 1 API request. Recommended values will allow up to 5 browser sessions / API requests to work simultaneously.

## Prerequisites

EAS Client does not require installation of any additional software to function. The application is built using .NET 8 in self-contained mode. So, all required libraries are already embedded into the executable.

In case you are facing dependency-related issues while trying to launch EAS Client on Linux, you can install [.NET Runtime](https://dotnet.microsoft.com/download/dotnet/8.0). Though it won't be used by EAS Client, installing it will ensure that all dependencies are present.
