import sys
from time import sleep

import boto3


def receive_message(url: str) -> None:
    """Receive messages from an SQS queue and delete them after processing."""
    sqs_client = boto3.client("sqs", region_name="us-east-1")
    while True:
        print("Aguardando mensagens...")
        sqs_message = sqs_client.receive_message(QueueUrl=url, VisibilityTimeout=10)
        for message in sqs_message.get("Messages", []):
            print(f"Mensagem Recebida: {{'message': {message['Body']!r}}}")
            sqs_client.delete_message(
                QueueUrl=url, ReceiptHandle=message["ReceiptHandle"]
            )
        sleep(10)


def main():
    if len(sys.argv) > 1:
        url_sqs = sys.argv[1]
        receive_message(url=url_sqs)


if __name__ == "__main__":
    main()
