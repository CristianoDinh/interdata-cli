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
#parser.usage
parser.prog = "./url.exe"
parser.description = (
    "╔════✨ Presign url file to send to other viewers in a particular time✨ ════╗\n"
)
parser.add_argument("bucket_source_name", help = ":S3 bucket source of file to be presigned", type = str)
parser.add_argument("file_name", help = ":File needs presigning name", type = str)
parser.add_argument("expires_in", help = ":Expiration time (in seconds)", type = int)

args : Namespace = parser.parse_args()

BUCKET_SOURCE = args.bucket_source_name
FILE_NAME = args.file_name
EXPIRES = args.expires_in

try:
    url = s3.generate_presigned_url(
        ClientMethod='get_object',
        Params={
            'Bucket': BUCKET_SOURCE,
            'Key': FILE_NAME
        },
        ExpiresIn = EXPIRES
    )
    print(f"URL: \033[1;4m{url}\033[0m")
except Exception as e:
    print(f"Error when generating presigned url: {e}")
