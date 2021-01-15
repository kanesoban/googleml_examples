## Setup

### Installin google cloud SDK

Follow this

https://cloud.google.com/sdk/docs/quickstart#deb

OR

these steps:

Add the Cloud SDK distribution URI as a package source (check first if it is already added)

`
echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
`

Make sure you have apt-transport-https installed:

`
sudo apt-get install apt-transport-https ca-certificates gnupg
`

`
echo "deb https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
`

Import the Google Cloud public key:

`
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key --keyring /usr/share/keyrings/cloud.google.gpg add -
`

`
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
`

Update and install the Cloud SDK:

`
sudo apt-get update && sudo apt-get install google-cloud-sdk
`

Install python api for sdk:

`
sudo apt-get install google-cloud-sdk-app-engine-python
`
`
sudo apt-get install google-cloud-sdk-app-engine-python-extras
`

Run gcloud init to setup:

`
gcloud init
`

### Install python requirements

`
conda env create -f conda/requirements.yml
`

`conda activate googlecloud`

### Select or create a Google Cloud project

https://console.cloud.google.com/projectselector2/home/dashboard?_ga=2.79168657.464093905.1610738268-1467417966.1610492912&pli=1

Enable the AI Platform Training & Prediction and Compute Engine APIs.

https://console.cloud.google.com/flows/enableapi?apiid=ml.googleapis.com,compute_component&_ga=2.242232583.464093905.1610738268-1467417966.1610492912



References:
* https://cloud.google.com/ai-platform/docs/getting-started-keras