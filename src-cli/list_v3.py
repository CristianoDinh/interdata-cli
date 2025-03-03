"""
This version is upgraded from list_v3.py(Ver1)
"""

from argparse import ArgumentParser, Namespace
import boto3, sys, os
from datetime import datetime
from dotenv import load_dotenv

parser = ArgumentParser()
#parser.usage
parser.prog = "./list.exe"
#parser.description = "Download your required file from Cloud Object Storage AWS-S3 -> Local storage"
parser.add_argument("bucket_name", help = ":AWS-S3 bucket name", type = str, nargs = "?")

group = parser.add_mutually_exclusive_group()
group.add_argument("-ab", "--allBuckets", help = ":List all S3 buckets", action = "store_true")
group.add_argument("-ao", "--allObjects", help = ":List all S3 objects", action = "store_true")

args : Namespace = parser.parse_args()

# Load file .env
load_dotenv()

# Read parameter from .env (environment variable)
ENDPOINT_URL = os.getenv('S3_ENDPOINT')
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_REGION = os.getenv('REGION_NAME')

# Initialize s3 client with Endpoint and Authenticate
s3 = boto3.client(
  's3',
        endpoint_url=ENDPOINT_URL,
        aws_access_key_id = AWS_ACCESS_KEY_ID,
        aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
        region_name=AWS_REGION
)

BUCKET_NAME = args.bucket_name

#1. List all S3 buckets
def list_all_buckets():
    try:
        response = s3.list_buckets()
        #Sorted buckets with Attribute ["CreationDate"]
        sorted_bucks = sorted(response['Buckets'], key = lambda bucket: bucket['CreationDate'], reverse = True)
        print('All existing AWS S3 buckets: ')
        print('|---|-----------------------------------|-------------------|')
        print('|No.|            Bucket Name            |   Creation Date   |')
        print('|---|-----------------------------------|-------------------|')
        if 'Buckets' in response:
            for index, bucket in enumerate(sorted_bucks, start = 1):
                creation_date = bucket['CreationDate']
                formatted_date = creation_date.strftime('%d/%m/%y %H:%M:%S')
                print(f"[{index:^3}] {bucket["Name"]:<34}| {formatted_date} |")
        else:
            print("No buckets found or not existing.")
        print('|---|-----------------------------------|-------------------|\n')
    except Exception as e:
        print(f"Error listing buckets: {e}")


#2. List all objects in S3 buckets
def list_all_objects(bucketName):
    try:
        response = s3.list_objects(Bucket=bucketName)
        #Sorted objects in bucket with Attribute Content['Last modified']
        sorted_objs = sorted(response['Contents'], key = lambda obj : obj['LastModified'], reverse = True)
        print(f"All existing objects in S3 bucket '{bucketName}'")
        print('|---|-------------------------------|---------------------------|')
        print('|No.|          Object Name          |       Last Modified       |')
        print('|---|-------------------------------|---------------------------|')
        if 'Contents' in response:
            for index, obj in enumerate(sorted_objs, start = 1):
                creation_date = obj['LastModified']
                formatted_date = creation_date.strftime('%d/%m/%y %H:%M:%S')
                print(f"[{index:^3}] {obj['Key']:<30}| {formatted_date:^25} |")
        else:
            print(f"No objects found or not existing in bucket '{BUCKET_NAME}'.")
        print('|---|-------------------------------|---------------------------|\n')
    except Exception as e:
        print(f"Error listing objects in bucket '{BUCKET_NAME}': {e}")


if args.allObjects:
    if not BUCKET_NAME:
        print("Error: You must specify a bucket name when using the --allObjects option.")
        sys.exit(1)
    list_all_objects(BUCKET_NAME)
elif args.allBuckets:
    list_all_buckets()
else:
    print("Error: Please provide an option (-ab | --allBuckets or -ao | --allObjects) to proceed.")
    sys.exit(1) #Exit program with error status.