import boto3

# Create S3 client
s3 = boto3.client('s3')

bucket_name = "my-unique-bucket-12345-balaji"
object_name = "Hello.txt"   # file in S3
download_name = "downloaded-balaji.txt"  # file name locally

# Download from S3 → local
s3.download_file(bucket_name, object_name, download_name)

print(f"✅ File '{object_name}' downloaded as '{download_name}'")
