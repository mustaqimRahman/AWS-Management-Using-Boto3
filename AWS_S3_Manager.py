# @Author: mustaqim
# @Date:   2016-11-16T18:29:46+01:00

print """
Welcome to S3 Manager. With this program you can do the following:
1. List Bucket
2. Create Bucket
3. Delete Bucket
4. Upload Files to Specific Bucket
5. Delete FIles form a Specific Bucket
"""

prompt = '> '

def listBucket():
    import boto3
    s3 = boto3.resource('s3')
    client = boto3.client('s3')
    count = 0
    for bucket in s3.buckets.all():
        print(bucket.name)
        count += 1
    print "\nTotal Buckets: {}\n".format(count)

    main()

# Code for creating bucket in amazon aws s3
def createBucket():
    import boto3
    import botocore

    # Create a boto3 resource of type S3
    s3 = boto3.resource('s3')
    # Create a client
    client = boto3.client('s3')

    print "Welcome to the create Bucket function"
    bucketName = raw_input("Provide a bucket name :")
    serverName = raw_input("Provide a serverName[ex:'EU', 'eu-west-1', 'us-west-1']:")

    try:
        kw_args = {
            'Bucket': bucketName,
            'ACL': 'private',
            'CreateBucketConfiguration': {
                  'LocationConstraint': serverName
             }
        }
        client.create_bucket(**kw_args)
        print "Your Bucket has been created successfully"
    except botocore.exceptions.ClientError as e:
        print e

    askUser = raw_input("Do you want to create another bucket(y/n)?")
    if askUser == "y":
        createBucket()
    else:
        main()

#code for deleting bucket from amazon aws s3
def deleteBucket():

    import boto3
    print "Welcome to the delete bucket function"
    s3 = boto3.resource('s3')
    # creating client
    client = boto3.client('s3')
    userOpenion = raw_input("do you want to see a list of existing Buckets(y/n):")
    if userOpenion == "n":
        bucketName = raw_input("Which bucket you want to delete :")

        print "Deleting bucket {}".format(bucketName)
        response = client.delete_bucket(
            Bucket=bucketName
        )
        print "Bucket successfully deleted"
    elif userOpenion == "y":
        listBucket()
        bucketName = raw_input("Which bucket you want to delete :")

        print "Deleting bucket {}".format(bucketName)
        response = client.delete_bucket(
            Bucket=bucketName
        )
        print "Bucket successfully deleted"

    askUser = raw_input("Do you want to delete another bucket(y/n)?")
    if askUser == "y":
        deleteBucket()
    else:
        main()

#code for uploading file to a bucket
def uploadFile():
    import boto3
    print "Welcome to the upload file function"
    # connection with s3
    s3 = boto3.resource('s3')

    # creating client
    client = boto3.client('s3')

    docName= raw_input("Enter the file name:")
    bucketName = raw_input("Enter the bucket name:")
    key = raw_input("Insert display name for the file in s3:")
    client.upload_file(docName, bucketName, key)
    # s3.Bucket('mustaqim1').upload_file('aaaa.txt', 'hello.txt')

    print "File Uploaded Successfully"

    askUser = raw_input("Do you want to upload another file(y/n)?")
    if askUser == "y":
        uploadFile()
    else:
        main()

#code for deleting file from a bucket
def deletefile():
    import boto3
    s3 = boto3.resource('s3')
    # creating client
    client = boto3.client('s3')
    print "Welcome to the delete file function "

    bucketName = raw_input("Enter the bucket name:")
    docName = raw_input("Enter the file name:")
    response = client.delete_object(
        Bucket=bucketName,
        Key=docName
    )
    print "Delete Status:",
    print bool(response)

    askUser = raw_input("Do you want to delete another file(y/n)?")
    if askUser == "y":
        deletefile()
    else:
        main()


# This is the main function
def main():
    print "What do you want to do(listBucket/createBucket/deleteBucket/uploadFile/deleteFile)"
    print prompt,
    task = raw_input()

    if task == "createBucket":
        createBucket()
    elif task == "listBucket":
        listBucket()
    elif task == "deleteBucket":
        deleteBucket()
    elif task == "uploadFile":
        uploadFile()
    elif task == "deleteFile":
        deletefile()
    else:
        print "Thank you for using S3 Manager"

main()
