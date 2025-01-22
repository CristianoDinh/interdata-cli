from argparse import ArgumentParser, Namespace
import boto3

parser = ArgumentParser()

#parser.usage = 'Using the program like this...'
parser.prog = "./copy.exe"
parser.description = (
    "╔════✨ Copy your required file from one bucket ➡️ another✨ ════╗\n"
)

parser.add_argument("bucket_source_name", help = ":Name of the S3 source bucket", type = str)
parser.add_argument("file_source_name", help = ":Name of file in S3 source bucket", type = str)
parser.add_argument("bucket_destination_name", help = ":Name of the S3 destination bucket will be copied to", type = str)
parser.add_argument("new_file_name", help = ":Name of file copied in S3 destination bucket", type = str)

args : Namespace = parser.parse_args()
s3 = boto3.client('s3', region_name = 'ap-southeast-1')

SOURCE_BUCKET = args.bucket_source_name
SOURCE_FILE = args.file_source_name
DES_BUCKET = args.bucket_destination_name
DES_FILE = args.new_file_name

try:
    s3.copy_object(
        # ACL = 'public-read',
        CopySource = f"{SOURCE_BUCKET}/{SOURCE_FILE}",
        Bucket = DES_BUCKET,
        Key = DES_FILE,
    )
    print(f"Copied {SOURCE_FILE} in bucket '{SOURCE_BUCKET}' to '{DES_BUCKET}' successfully.")
except Exception as e:
    print(f"Failed to copy {SOURCE_FILE} to '{DES_BUCKET}'!\nError: {e}")

