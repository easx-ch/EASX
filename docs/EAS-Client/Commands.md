This document contains detailed description of all commands that are supported by EASX Client.

To run any of these, you'll need to open a command line / terminal and navigate to the location of EAS Client executable. Next, you can execute commands like this:

`EASClient.exe --host`

Some of the commands require a parameter. Usually it's a path to file or folder. All paths can be absolute, relative or in any other format supported by the OS. You can omit quotes in case a path contains no whitespaces. Assuming `EASClient.exe` is located in `C:\eas`, all following formats are equivalent:

`EASClient.exe --receive incoming`

`EASClient.exe --receive "incoming"`

`EASClient.exe --receive C:\eas\incoming`

`EASClient.exe --receive "C:\eas\incoming"`

## Commands list

**--host**

Launch the client in host mode. An instance of Web GUI and APIs will be hosted locally (http://localhost:5000 by default).

**--debug**

This parameter can be used together with any command to enable verbose logs. For example, launching a client with `--debug --host` instead of just `--host` will make it log debug information and server responses.

Example output:

```txt
[13:44:33 DBG] Hosting starting
[13:44:33 INF] Now listening on: http://localhost:5000
[13:44:33 DBG] Loaded hosting startup assembly EASClient
[13:44:33 INF] Application started. Press Ctrl+C to shut down.
[13:44:33 INF] Hosting environment: dev
[13:44:33 INF] Content root path: C:\eas
[13:44:33 DBG] Hosting started
```

**--list-in**

Get the list of incoming document metadata and print them into console.

Example output:

```txt
Found 2 incoming documents:

Id  : 8afb7267-b546-4b17-8881-ded17aa9369b
Date: 16.07.2021 8:47:58
Type: http://exchange.aeis.ch/xsd/FZL-1.5
From: CHE109405059
To  : TESTCLIENTA


Id  : 454fbcf4-6e55-401b-b9ff-56f08c2330ce
Date: 16.07.2021 14:59:52
Type: http://exchange.aeis.ch/xsd/FZL-1.5
From: CHE109691681
To  : TESTCLIENTA


All Done
```

**--send "path"**

Send all files from the specified folder. Right now, EAS Client supports XML files with 1.5 schema version. This command automatically encrypts, signs, uploads each document and sends it to receiver, determined by parsing an XML file. After the document was sent, it is moved to the "sent" folder.

Example output:

```txt
Sending 2 files from "outgoing":
sample1.xml - signed - encrypted - uploaded - sent - moved to sent subfolder
sample2.xml - signed - encrypted - uploaded - sent - moved to sent subfolder
All Done
```

**--receive "path"**

Receive all incoming documents to the specified folder. The command automatically downloads all documents, decrypts them, stores to the folder, removes from incoming and sends receipts.

Example output:

```txt
Connecting
Receiving 2 files to "incoming":
8afb7267-b546-4b17-8881-ded17aa9369b - downloaded - received
960ac6af-3a82-4257-a7d5-8f7e867f86af - downloaded - received
All Done
```

**--get-receipts "path"**

Get all receipts and save them to the specified folder. This command will also automatically remove receipts from the server side after downloading.

Example output:

```txt
Connecting
Receiving 2 files to "receipts":
df25485f-89d9-4162-a3cd-f8e3d83a440d - downloaded - cleared
e6875ec2-634b-4c02-9e14-ed20efbcd9d0 - downloaded - cleared
All Done
```

Example file:
`0ad62440-f3ad-411b-a5d8-7794a2c8367c.json`

```json
{
  "Id": "e6875ec2-634b-4c02-9e14-ed20efbcd9d0",
  "ReceivedDate": "2021-07-20T08:14:47.6545973Z",
  "TransferId": "a54c19ea-110f-4785-a5e0-b43662fad41d",
  "TransferSenderId": "TESTCLIENTA",
  "TransferReceiverId": "CHE109691681",
  "Code": "Success",
  "Message": null
}
```

**--generatekeys "fileprefix" --keysize [<3072|4096>]**

Generate RSA key pairs (**3072-bit by default, 4096-bit available**).  
The `--keysize` option is optional and allows specifying the key size.  
The command will generate two `.pem` files using the provided `fileprefix`:
- `fileprefix-private-key.pem` (**private key**)  
- `fileprefix-public-key.pem` (**public key**)  

These keys can later be used while configuring the EAS Client.

### Example Output:**
```txt
 Generating 3072-bit private/public key pair...
 Private key file sample-private-key.pem generated
 Public key file sample-public-key.pem generated
 All Done
```

Example private key:
`sample-private-key.pem`

```txt
-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAvz9a0E/wfWHNwxoeDPUgTZMCQNcoRDRybObnPtYi7OEnUM420
cnvQ6/dSVn0FWx49CPSyeEeMzBeqHKqFPI/vC3hw8tm8PYxjNEVi/0KKy7df/Ew+/
bpoRtvVlqppIVXaG/j1PwF7/qVt8Pdl715I5qxylhqrest1d2BoxyOPmr01UIAk5t
9fuNxXhhAZ06jq420KdWty1MpCUATNFPyDk6JYb7V+yd6hh2TpFcbB6egMlgkzbnY
rS668ya6d2XSRch4AIxnpFmwV9K9TvXSa13+UW1Z1qjhb/zKdm49kKWSljC/cRUnZ
OCQ6TrNKuYyo1/qoaptdgWMMm9HyZzWxQIDAQABAoIBABh0RWx1jE67/s9/u2/0uB
izP4qC+IcgHbGHJPKH9xdLAvf2JlRU+d8x0Z3bfrZulFjDa+ScgHwTJ0dqwgzDnRq
20zNyAsu070kOQy8PQAmdiH0fnh/Zxq3vECF+nkqHMlIMXJmTUD8LT7Gbve31MFQ5
J5q0C5AJjmbWWAk/UYDxe2QJ1/dQO9D0IisgF1UMV5pkB+BUXiUJ237G++4K4HhFB
NklfakP4X4Q1Wde/UjX9z+VvTPB4WGQxQZvtDOwo8IHs/6DRTXnyRy2NReGs9DMTd
pbM3NkmOHS91/FjIpwPYRMcCI9QMMmRF0VEHn8IbAUo+OeQFN1NDbLWR2sjVECgYE
A8iBeb8Gtuo8TN0uUJ2ion7L2ZzR59jq/itM/PHcEUZVzgJTqErpLfHTaG224p54a
+QmB0WF3f6c9K0lfHgr7A5ZyonpntkQTVUnjHJy0PoGyjUmI6huUnHSfcCWST0lBK
SiYrcvnAa64ABnk/Ib8hh9Tfjmt/1Up0HodKflbmVMCgYEAyjSq/SwaY7XFn2UsaI
JiqnC4d/XW79qgjfCFN11sgq6yzD9BzDfFEFZa8oZmll2JOoqQSJ+7SWYrCUWt3oz
F+3L8sQq/hfXvI1Foqyb1l5gKD+0ZagfRDazrbgclmvEZJAElju+tYi+mkHaT18G1
wC7Ol+ZkqjJJG8QQn09JlIcCgYBGDhuE1lL/0XnL2/BH3r47RrqIbeSD28ej0S9Qv
VbgjA9ZOrznIkPJBL4+hWaSCOrg92E6RasfojHOnnII7UBnb1ZHsIblc5jsam5tzu
FP3JLe0lHs+oHrKsse1aAZlKZn1DkowABcukK+tL9OWXgjDllIAkRXxjpM+agKhv1
7xQKBgQCKwVGEobsKKTYPhzHOFYr3QpqTVxPDS9dZD2+a6nUHyDHRjqbsKGkGKPwH
6MqE7HK6xVL1QwcV+xIVLsd9LES/o8xbAPEkT/tl1PtqVzW4bRCalS0XYX3HUJ3Nx
wG7LS7/Ufof98CW2/QEthoFuFusIXKLMgJp+E/KyeROLe5kCQKBgB77bIeSGhdFpn
OumV63qHZK0sFqeaeaBjbIaz+jcuUo//VVpJHUpV6+zzN2zbw6WYvB0Bpa2MrZJnm
RYu1s8MsrEv8yHLjRzeE27l3dUM4z5Wa2v+dFf4Pp0uOoY7t0I8DZzvdN4QPgsP3d
AWTrXJ3/ej6c9AI2EtctY6aSWSQx
-----END RSA PRIVATE KEY-----
```

Example public key:
`sample-public-key.pem`

```txt
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvz9a0E/wfWHNwxoeDPUgT
ZMCQNcoRDRybObnPtYi7OEnUM420cnvQ6/dSVn0FWx49CPSyeEeMzBeqHKqFPI/vC
3hw8tm8PYxjNEVi/0KKy7df/Ew+/bpoRtvVlqppIVXaG/j1PwF7/qVt8Pdl715I5q
xylhqrest1d2BoxyOPmr01UIAk5t9fuNxXhhAZ06jq420KdWty1MpCUATNFPyDk6J
Yb7V+yd6hh2TpFcbB6egMlgkzbnYrS668ya6d2XSRch4AIxnpFmwV9K9TvXSa13+U
W1Z1qjhb/zKdm49kKWSljC/cRUnZOCQ6TrNKuYyo1/qoaptdgWMMm9HyZzWxQIDAQ
AB
-----END PUBLIC KEY-----
```

**--help**

Prints client version and a list of supported commands into console.

Example output:

```txt
EAS Client version 0.8.3.0

The app can be used to call EAS Hub and Directory APIs from the command line. It is also possible to run the app in host mode to get local Web UI and a local instance of all APIs.
Use one of the following arguments:
 --list-in : Get the list of incoming document IDs
 --send "path" : Send all files from the specified folder
 --receive "path" : Receive all incoming files to the specified folder.
 --get-receipts "path" : Get all receipts to the specified folder.
 --generatekeys [fileprefix] --keySize [keySize] : Generate 3072bit (default) or 4096bit private/public key files.
 --host : Run the app in hosted mode.

Navigate to the following URL for more information: https://docs.easx.ch
```
