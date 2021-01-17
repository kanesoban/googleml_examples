## Setup

### Installing google cloud SDK

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

Follow the instructions...

### Install python requirements

`
conda env create -f conda/requirements.yml
`

`conda activate googlecloud`

### Select or create a Google Cloud project

https://console.cloud.google.com/projectselector2/home/dashboard?_ga=2.79168657.464093905.1610738268-1467417966.1610492912&pli=1

Enable the AI Platform Training & Prediction and Compute Engine APIs.

https://console.cloud.google.com/flows/enableapi?apiid=ml.googleapis.com,compute_component&_ga=2.242232583.464093905.1610738268-1467417966.1610492912


### Get necessary information to run a cloud training

You can start a cloud training job with
`
sh train_cloud.sh
`

but you will need at minimum this information to run it:
* compute region
* bucket name where to run job
* google application credentials file

#### Get compute region

Running

`
gcloud config list
`

current configuration details such as current compute region.

#### Get bucket name

Go to

https://console.cloud.google.com/home/dashboard

select a project, and under 'Resources' click 'Storage'.

Here you can see names for existing buckets. Use one or create one here.

#### Get credentials file

TODO

## Get information about a 'run' (e.g. source files, outputs etc)

Go to

https://console.cloud.google.com/home/dashboard

select a project, and under 'Resources' click 'Storage'.

Here you can see names for existing buckets. Select bucket where the run happened.
Here select the job directory for the training.
You should see information for a run.

## Run training in cloud

Example command to run training in cloud:

`
gcloud ai-platform jobs submit training <JOB NAME>
  --package-path <package path>
  --module-name <module name>
  --region <region>
  --config <config yaml>
  --python-version <python version>
  --runtime-version <runtime version>
  --job-dir <job dir>
  --stream-logs
`

* package path: path to the root directory python package e.g. "mnist"
* module name: full name of the module e.g. "mnist.task"

OR run

`train_cloud.sh`


References:
* https://cloud.google.com/ai-platform/docs/getting-started-keras
* https://cloud.google.com/sdk/docs/quickstart


