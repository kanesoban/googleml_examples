#!/bin/bash


export REGION="europe-west1"
export BUCKET_NAME="default"
export GOOGLE_APPLICATION_CREDENTIALS="credentials.json"


JOB_NAME="keras_mnist"
JOB_DIR="gs://$BUCKET_NAME/keras-job-dir"

gcloud ai-platform jobs submit training $JOB_NAME \
  --package-path mnist/ \
  --module-name mnist.task \
  --region $REGION \
  --python-version 3.6.7 \
  --runtime-version 1.15 \
  --job-dir $JOB_DIR \
  --stream-logs
