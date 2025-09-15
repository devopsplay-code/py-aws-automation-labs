# delete_bucket.py
import boto3

# Step 1: Connect to S3 in your region (Stockholm)
s3 = boto3.client("s3", region_name="eu-north-1")

# Step 2: Name of the bucket to delete
bucket_name = "my-unique-bucket-12345-balaji"  # change to your bucket name

# Step 3: Delete the bucket
response = s3.delete_bucket(Bucket=bucket_name)

print(f"🗑️ Bucket '{bucket_name}' deleted successfully!")
