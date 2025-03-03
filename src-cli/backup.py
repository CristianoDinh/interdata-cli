from argparse import ArgumentParser, Namespace
import os, boto3, zipfile
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
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


def download_and_zip(bucket_name, output_zip):
    """
    Tải tất cả các file trong bucket từ S3 và nén thành file zip.

    Args:
        bucket_name (str): Tên bucket S3.
        output_zip (str): Đường dẫn file zip sẽ tạo ra.
    """

    try:
        # Get all objects from bucket
        response = s3.list_objects_v2(Bucket=bucket_name)
        if 'Contents' not in response:
            print(f"Bucket '{bucket_name}' is empty or not existing.")
            return

        # Create zip file
        with zipfile.ZipFile(output_zip, 'w') as zipf:
            print(f"Downloading and compressing files from bucket '{bucket_name}'...")
            for obj in response['Contents']:
                file_key = obj['Key']
                local_file_path = os.path.join('temp', file_key) #temporary save to local path: temp/file_key

                # Make dir if necessary
                os.makedirs(os.path.dirname(local_file_path), exist_ok=True)

                # Tải file từ S3
                s3.download_file(bucket_name, file_key, local_file_path)
                print(f"Downloading file: {file_key}")

                # Thêm file vào file zip
                zipf.write(local_file_path, arcname=file_key)
                print(f"Adding file '{file_key}' to zip file.")

                # Remove file from temp after added file to zip.
                os.remove(local_file_path)

        print(f"All files you need has been compressed to '{output_zip}'.")

    except NoCredentialsError:
        print("Not finding AWS credentials information.")
    except PartialCredentialsError:
        print("AWS credentials not completed.")
    except Exception as e:
        print(f"Existing errors: {e}")


if __name__ == "__main__":
    # CLI with argparse
    parser = ArgumentParser(description="Backup all file from S3 bucket && compress to zip file.")
    parser.prog = "./backup.exe"
    parser.add_argument("bucket_name", help=":Name of buckets need to be backup.")
    parser.add_argument("output_zip_path", help=":Path to output zip file at local.")
    args : Namespace = parser.parse_args()

    download_and_zip(args.bucket_name, args.output_zip_path)
