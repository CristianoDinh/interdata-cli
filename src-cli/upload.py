from argparse import ArgumentParser, Namespace
import boto3, os
from dotenv import load_dotenv

#=====================================================================
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
#=====================================================================

parser = ArgumentParser()
#parser.usage = 'Using the program like this...'
parser.prog = "./upload.exe"
parser.description = "Upload your required file from Local -> Cloud Object Storage AWS-S3"
parser.add_argument("file_source", help = ":Path of the file to be uploaded", type = str)
parser.add_argument("bucket_name", help = ":The S3 bucket will be upload to", type = str)
parser.add_argument("new_file_name", help = ":Name of the uploaded file in that bucket", type = str)

args : Namespace = parser.parse_args()

FILE_SOURCE = args.file_source
BUCKET_NAME = args.bucket_name
NEW_FILE_NAME = args.new_file_name

try:
    with open(FILE_SOURCE, 'rb') as file:
        s3.upload_fileobj(
            file,
            BUCKET_NAME,
            NEW_FILE_NAME,
            #ExtraArgs={"ACL": ""}
        )
    print(f"Uploaded new file '{NEW_FILE_NAME}' to '{BUCKET_NAME}' ")
except Exception as e:
    print(f"Failed to upload your file to bucket '{BUCKET_NAME}'\nReason: {e}")






