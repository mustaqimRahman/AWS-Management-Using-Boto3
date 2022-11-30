import boto3
import config

# Defining an S3 client
# S3 client lets you read, write objects in S3
s3 = boto3.client("s3", aws_access_key_id=config.access_key,
                  aws_secret_access_key=config.secret_access_key)

# Declaring Local File Path and File Name, which will be uploaded to S3

bucket_name = config.bucket_name


def upload_file(file_name):

    raw_file_name = file_name.split('\\')

    object_name = raw_file_name[len(raw_file_name)-1]

    try:
        # Passing 3 values in upload file, (1)Whom we are uploading, (2)Which bucket, (3)New File Name
        response = s3.upload_file(file_name, bucket_name, object_name)
        print('The File Was Uploaded To S3 Bucket Successfully!')
    except Exception as e:
        print(e)
        return False
    return True
