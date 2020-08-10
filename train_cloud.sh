#!/bin/bash


export REGION="europe-west1"
export BUCKET_NAME="default"
export GOOGLE_APPLICATION_CREDENTIALS="/home/cszsolnai/Projects/googleml_examples/credentials.json"


JOB_NAME="keras_mnist_${USER}_$(date +%Y%m%d_%H%M%S)"
export STORAGE_BUCKETNAME=tensorflow-course-256109
JOB_DIR="gs://$STORAGE_BUCKETNAME/keras-job-dir"


gcloud ai-platform jobs submit training $JOB_NAME \
  --package-path mnist/ \
  --module-name mnist.task \
  --region $REGION \
  --config config.yaml \
  --python-version 3.7 \
  --runtime-version 2.1 \
  --job-dir $JOB_DIR \
  --stream-logs
