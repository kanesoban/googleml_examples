#!/bin/bash


export REGION="europe-west1"
export BUCKET_NAME="default"
export GOOGLE_APPLICATION_CREDENTIALS="credentials.json"

gsutil mb -l $REGION gs://$BUCKET_NAME

gcloud ai-platform local train \
  --package-path mnist \
  --module-name mnist.task \
  --job-dir output
