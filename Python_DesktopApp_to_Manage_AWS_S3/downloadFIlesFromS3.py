import boto3
import config

# Defining an S3 client
# S3 client lets you read, write objects in S3
s3 = boto3.client("s3", aws_access_key_id=config.access_key,
                  aws_secret_access_key=config.secret_access_key)

# Declaring Local File Path and File Name, which will be uploaded to S3

bucket_name = config.bucket_name
download_path = config.download_path


def downloadFile(file_name):

    s3.download_file(bucket_name, file_name, download_path + file_name)
# downloadFile('Hero.JPG')
