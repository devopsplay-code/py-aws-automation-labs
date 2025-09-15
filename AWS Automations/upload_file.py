# upload_file.py
import boto3

# Step 1: Connect to S3 in your region (Stockholm)
s3 = boto3.client("s3", region_name="eu-north-1")

# Step 2: Define bucket name and file details
bucket_name = "my-unique-bucket-12345-balaji"   # 🔹 your bucket name
file_name = "sample.txt"                        # 🔹 local file you want to upload
object_name = "sample.txt"                      # 🔹 name inside S3 (can rename if you want)

# Step 3: Upload the file
s3.upload_file(file_name, bucket_name, object_name)

print(f"📂 File '{file_name}' uploaded to bucket '{bucket_name}' as '{object_name}' ✅")
