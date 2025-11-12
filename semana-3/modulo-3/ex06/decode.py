import base64
import boto3
from botocore.exceptions import ClientError
import io
import sys


def decode_image(base64_str: str) -> bytes:
    """Decode a base64 string to bytes."""
    return base64.b64decode(base64_str)


def upload_image_s3(image_bytes: bytes, image_filename: str, bucket_name: str='42sp-imilhome-bucket') -> None:
    """Upload image to s3"""
    image_file_object = io.BytesIO(image_bytes)
    s3_cliente = boto3.client("s3",region_name='us-east-1')
    key = image_filename
    try:
        s3_cliente.upload_fileobj(
            Fileobj=image_file_object, 
            Bucket=bucket_name, 
            Key=key
        )
    except ClientError as e:
        print(e)


if __name__ == "__main__":
    bucket_name = sys.argv[1]
    base64_str = sys.argv[2]
    with open(base64_str) as file:
        base64_lines = file.readline().replace("data:image/jpeg;base64,", "")
        image_bytes = decode_image(base64_lines)
        image_filename = base64_str.split('/')[-1].replace("txt", "jpg")
        
        upload_image_s3(image_bytes, image_filename, bucket_name)
        print(f"'{image_filename}' saved on bucket '{bucket_name}'!")
