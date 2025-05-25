import os
import boto3
from django.conf import settings


class S3SpacesUtility:

    @classmethod
    def get_spaces_client(cls):
        return boto3.client(
            "s3",
            region_name="nyc3",
            endpoint_url="https://nyc3.digitaloceanspaces.com",
            aws_access_key_id=os.getenv("SPACES_ACCESS_KEY"),
            aws_secret_access_key=os.getenv("SPACES_SECRET_KEY"),
        )
