# AWS-S3-Management-Using-Boto3

##Introduction
Boto3 is the Amazon Web Services (AWS) Software Development Kit (SDK) for Python, which allows Python developers to write software that makes use of Amazon services like S3 and EC2. Boto provides an easy to use, object-oriented API as well as low-level direct service access. Check out the latest documantation [here](https://boto3.readthedocs.io/en/latest/).

####This program can do basic Amazom AWS S3 management tasks, such as - Showing a list of existing bucket, Creating bucket, Deleting bucket, Uploading files to a bucket and Deleting files from a bucket.

##Access to Amazon AWS 
1.Create an Amazon AWS account. For students it is recommened to have an AWS Educate account.

2.Create aws_access_key_id and aws_secret_access_key. To do so read this [documentation](http://docs.aws.amazon.com/general/latest/gr/managing-aws-access-keys.html)

##Configuration in your PC
1.Install pip in your machine.
```
$ sudo easy_install pip
```
2.Install aws command line
```
$ sudo pip install awscli --ignore-installed six
```
3.Configure aws_access_key_id and aws_secret_access_key
```
$ aws configure 
```
```
aws_access_key_id = YOUR_KEY
aws_secret_access_key = YOUR_SECRET
region=us-east-1
```
4.Install Virtualenv.
```
$ [sudo] pip install virtualenv
```
5.Create a virtual environment for python in any directory(you can put any name instead of ENV).
```
$ virtualenv ENV
```
6.Activate the virtual environment 
```
$ source ENV/bin/activate
```
7.Install boto3 inside the virtual environment. No need to use sudo inside virtual environment.
```
$ pip install boto3
```
8.Clone the "AWS_S3_Manager.py" to a directory.

9.Run the file 
```
$ python AWS_S3_Manager.py
```
You are all set to create/delete bucket in s3 and uoload/delete file in s3 bucket.

