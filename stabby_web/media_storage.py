from storages.backends.s3boto3 import S3Boto3Storage
import os


class MediaStorage(S3Boto3Storage):
    bucket_name = os.getenv("SPACES_BUCKET_NAME")
    custom_domain = False  # Ensures private access
    default_acl = "private"
    file_overwrite = False
    location = os.getenv("SPACES_LOCATION", "images")
