import boto3
import sys
from botocore.exceptions import ClientError

def create_presigned_url(bucket_name, object_name, expiration=600):
    """Generate a presigned URL to share an S3 object

    :param bucket_name: string
    :param object_name: string
    :param expiration: Time in seconds for the presigned URL to remain valid
    :return: Presigned URL as string. If error, returns None.
    """

    s3_client = boto3.client('s3')
    try:
        response = s3_client.generate_presigned_url(
            ClientMethod='get_object',
            Params={'Bucket': bucket_name, 'Key': object_name},
            ExpiresIn=expiration,
        )
    except ClientError as e:
        raise e
    return response
    
if __name__ =='__main__':
    bucket_name = sys.argv[1]
    image_name = sys.argv[2]
    presigned_url = create_presigned_url(bucket_name,image_name)
    print(presigned_url)