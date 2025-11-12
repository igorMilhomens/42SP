#!/bin/bash


aws s3api put-public-access-block \
    --bucket "42sp-imilhome-bucket" \
    --public-access-block-configuration "BlockPublicAcls=false,IgnorePublicAcls=false,BlockPublicPolicy=false,RestrictPublicBuckets=false"

aws s3api put-bucket-policy --bucket 42sp-imilhome-bucket \
    --policy file://policy.json

echo "Policy applied to bucket."