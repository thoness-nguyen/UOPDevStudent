# External URI Suitelets
The "Exernal URI Suitelet" provides the ability to launch HTML content hosted from an external server. The suitelet downloads the content and "re-serves" it as the suitelet response. Remote hosts currently must be whitelisted in the suitelet itself.

## Using the Suitelet
Send a GET to the suitelet URL with the following query parameters:

* **`url` (required):** The full URL to the remote content to load. The remote host must be whitelisted!
* **`bustCache`:** Use `bustCache=true` to force the suitelet to reload the content from the remote host. Otherwise, content will be cached on NetSuite's servers for up to 8 hours.

## Examples

#### Normal Usage
`https://system.netsuite.com/app/site/hosting/scriptlet.nl?script=1176&deploy=1&url=https://tcpsgpsatool.azurewebsites.net/#/projects/5707754`

#### Cache Busting
`https://system.netsuite.com/app/site/hosting/scriptlet.nl?script=1176&deploy=1&bustCache=true&url=https://tcpsgpsatool.azurewebsites.net/#/projects/5707754`

#### Search Formula Usage
`'<a href="/app/site/hosting/scriptlet.nl?script=1176&deploy=1&&url=https://tcpsgpsatool.azurewebsites.net/#/projects/'||{internalId}||'" target="_blank">Open in PSA Tool</a>'`
