#! /bin/bash

aws s3api create-bucket \
    --bucket 42sp-imilhome-bucket \
    --region us-east-1

aws s3 wait bucket-exists --bucket 42sp-imilhome-bucket