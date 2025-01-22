from argparse import ArgumentParser, Namespace
import boto3

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
s3 = boto3.client('s3', region_name='ap-southeast-1')

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
