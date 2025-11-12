#! /bin/bash

# aws s3api put-object \
#     --bucket 42sp-imilhome-bucket \
#     --key dev.env \
#     --body ../dev.env

aws s3 cp ../dev.env s3://42sp-imilhome-bucket/dev.env
