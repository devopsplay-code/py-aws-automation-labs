# create_bucket.py
import boto3

# Step 1: Connect to S3
s3 = boto3.client("s3")

# Step 2: Choose a bucket name (must be unique across all AWS)
bucket_name = "my-unique-bucket-12345-balaji"

# Step 3: Create the bucket
response = s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={
        'LocationConstraint': 'eu-north-1'  # change region if needed
    }
)

print(f"✅ Bucket '{bucket_name}' created successfully!")
