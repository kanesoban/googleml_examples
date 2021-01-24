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

Follow this (create service account)
https://cloud.google.com/docs/authentication/getting-started

Make sure that the right project is selected, because the credentials file will only work with it.

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

For more info on submitting a training job:

https://cloud.google.com/ai-platform/training/docs/using-gpus#submit-job

## Creating a project in google cloud console

Go here:
https://console.cloud.google.com/flows/enableapi?apiid=ml.googleapis.com,compute_component&_ga=2.242232583.464093905.1610738268-1467417966.1610492912

### Setup billing account 

You will need to link a billing account to a project to use it:
https://cloud.google.com/billing/docs/how-to/manage-billing-account

If you don't have any active billing accounts then either activate or make new account:
https://console.cloud.google.com/billing?_ga=2.12545969.464093905.1610738268-1467417966.1610492912

For reopening a closed account:
https://cloud.google.com/billing/docs/how-to/manage-billing-account#reopen_a_closed_billing_account

### Create bucket

https://cloud.google.com/ai-platform/training/docs/working-with-cloud-storage#cloud-storage-setup

or

https://console.cloud.google.com/storage/browser?_ga=2.15732659.464093905.1610738268-1467417966.1610492912&project=lunar-parsec-302010&prefix=


## Deleting instances after training

### Listing current instances

`
gcloud compute instances list
`

### Deleting instances

If you don't want to keep an instance which was used for training, you should delete it so that it doesn't
waste your money when it is being idle.

https://cloud.google.com/compute/docs/instances/deleting-instance

https://cloud.google.com/sdk/gcloud/reference/compute/instances/delete

## Troubleshooting

### I get "The project to be billed is associated with a closed billing account." when trying to start a training

Things to try in order:

* Try to enable billing in the project selector page.
* Try to reopen the billing account linked to the project if it is closed: https://cloud.google.com/billing/docs/how-to/manage-billing-account#reopen_a_closed_billing_account
* Create a new billing account if it cannot be reopened:
    * https://console.cloud.google.com/billing?project=&folder=&organizationId=0
    * link it to the project






References:
* https://cloud.google.com/ai-platform/docs/getting-started-keras
* https://cloud.google.com/sdk/docs/quickstart


