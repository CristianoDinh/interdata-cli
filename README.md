# CLI Data Management Tool

![AWS-S3](https://img.shields.io/badge/AWS-S3-orange?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

## 📌 Overview
This project is a **Command Line Interface (CLI) application** developed in Python that allows users to efficiently manage their data stored in **AWS S3**. It provides functionalities such as:
- Uploading, downloading, and listing objects in AWS S3 buckets.
- Moving and backing up files.
- Generating temporary URLs for S3 objects.

## ✨ Features
- **Connect to AWS S3**: Uses `boto3` to interact with Amazon S3 for file operations.
- **User-Friendly CLI**: Built with `argparse` for clear and simple commands.
- **Standalone Executable**: Packaged using `PyInstaller`, allowing users to run it without installing Python.

## 🚀 Installation
Ensure you have **Python 3.x** installed. Then, install dependencies:
```sh
pip install -r requirements.txt
```
To create an executable using **PyInstaller**:
```sh
pyinstaller --onefile your_script.py
```

## 🛠 Usage

### 🔹 Listing Buckets & Files
- List all S3 buckets:
  ```sh
  ./list.exe -ab
  ```
- List all objects in a specific bucket:
  ```sh
  ./list.exe -ao "your_bucket_name"
  ```

### 🔹 Upload & Download
- **Upload a file to S3**:
  ```sh
  ./upload.exe "local_file_path" "bucket_name" "new_file_name"
  ```
- **Download a file from S3**:
  ```sh
  ./download.exe "file_in_bucket" "bucket_name" "download_path"
  ```

### 🔹 Copy & Backup
- **Move a file from one bucket to another**:
  ```sh
  ./copy.exe "source_bucket" "source_file" "destination_bucket" "destination_file"
  ```
- **Backup all files in a bucket into a ZIP file**:
  ```sh
  ./backup.exe "bucket_name" "output_zip_path"
  ```

### 🔹 Generate Temporary URL
- Create a **temporary access link** for an S3 object:
  ```sh
  ./url.exe "bucket_name" "file_name" "expiration_time_seconds"
  ```

## 📜 Requirements
- Python 3.x
- `argparse` (for CLI argument parsing)
- `boto3` (for AWS S3 interactions)
- `pyInstaller` (for packaging the executable)

## 📝 License
This project is licensed under the **MIT License**.

---
⭐ **Don't forget to star this repository if you find it useful!** 🚀


