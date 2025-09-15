import boto3

# Create S3 client
s3 = boto3.client('s3')

# Your bucket name (replace with your actual bucket)
bucket_name = "my-unique-bucket-12345-balaji"

# List objects in the bucket
response = s3.list_objects_v2(Bucket=bucket_name)

# Check if bucket is empty or not
if 'Contents' in response:
    print(f"📋 Files inside bucket '{bucket_name}':")
    for obj in response['Contents']:
        print(f"  - {obj['Key']}")
else:
    print(f"⚠️ Bucket '{bucket_name}' is empty!")
