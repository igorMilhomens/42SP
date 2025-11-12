import sys

import boto3
from botocore.exceptions import ClientError


def send_message(url: str, msg: str) -> None:
    """Send a message to an SQS queue."""
    sqs_client = boto3.client("sqs", region_name="us-east-1")
    try:
        sqs_client.send_message(QueueUrl=url, MessageBody=msg)
    except ClientError as e:
        print(e)


def main():
    if len(sys.argv) > 1:
        url_sqs = sys.argv[1]
        msg = sys.argv[2]
        send_message(url=url_sqs, msg=msg)


if __name__ == "__main__":
    main()
