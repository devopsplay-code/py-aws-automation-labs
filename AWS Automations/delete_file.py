import boto3

# Step 1: Connect to S3
s3 = boto3.client("s3")

# Step 2: Bucket name + file name
bucket_name = "my-unique-bucket-12345-balaji"  # change to your bucket
file_name = "test.txt"  # change to the file you uploaded

# Step 3: Delete the file
s3.delete_object(Bucket=bucket_name, Key=file_name)  

print(f"🗑️ File '{file_name}' deleted successfully from bucket '{bucket_name}'!")
