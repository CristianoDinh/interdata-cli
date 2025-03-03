from argparse import ArgumentParser, Namespace
import boto3, sys
from datetime import datetime

parser = ArgumentParser()
#parser.usage
parser.prog = "./list.exe"
#parser.description = "Download your required file from Cloud Object Storage AWS-S3 -> Local storage"
parser.add_argument("bucket_name", help = ":AWS-S3 bucket name", type = str, nargs = "?")

group = parser.add_mutually_exclusive_group()
group.add_argument("-ab", "--allBuckets", help = ":List all S3 buckets", action = "store_true")
group.add_argument("-ao", "--allObjects", help = ":List all S3 objects", action = "store_true")

args : Namespace = parser.parse_args()
s3 = boto3.client('s3', region_name='ap-southeast-1')

BUCKET_NAME = args.bucket_name

#1. List all S3 buckets
def list_all_buckets():
    try:
        response = s3.list_buckets()
        #Sorted buckets with Attribute ["CreationDate"]
        sorted_bucks = sorted(response['Buckets'], key = lambda bucket: bucket['CreationDate'], reverse = True)
        print('All existing AWS S3 buckets: ')
        if 'Buckets' in response:
            for index, bucket in enumerate(sorted_bucks, start = 1):
                print(f"[{index:^5}] {bucket["Name"]:<30}| {bucket["CreationDate"]} |")
        else:
            print("No buckets found or not existing.")
    except Exception as e:
        print(f"Error listing buckets: {e}")


#2. List all objects in S3 buckets
def list_all_objects(bucketName):
    try:
        response = s3.list_objects(Bucket=bucketName)
        print('All existing AWS S3 objects: ')
        if 'Contents' in response:
            for index, obj in enumerate(response['Contents'], start = 1):
                print(f"[{index:^3}] {obj['Key']:<30}| {obj['LastModified']} |")
        else:
            print(f"No objects found or not existing in bucket '{BUCKET_NAME}'.")
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