#! /bin/bash

aws sqs send-message --queue-url http://sqs.us-east-1.localhost.localstack.cloud:4566/000000000000/42sp-fenunes--queue --message-body 'Olá SQS!'