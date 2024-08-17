import os
import hashlib
from azure.storage.blob import BlobServiceClient


# Retrieve the environment variable
secret_value = os.getenv('AZURE_STORAGE_ACCOUNT_KEY')

dummy_string = "does this work?"

print(dummy_string)


if secret_value:
    # Perform an operation using the secret
    hashed_value = hashlib.sha256(secret_value.encode()).hexdigest()
    print(f"Secret is set and its hash is: {hashed_value}")
else:
    print("Secret is not set.")


account_name = "yorkvilleworks9016610742"


if not account_key:
    raise ValueError("AZURE_STORAGE_ACCOUNT_KEY environment variable is not set.")

# Form the connection string
connection_string = f"DefaultEndpointsProtocol=https;AccountName={account_name};AccountKey={account_key};EndpointSuffix=core.windows.net"

container_name = "uploaded-files"

# Create a BlobServiceClient
print("Creating BlobServiceClient...")
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# List blobs in the container
blob_list = blob_service_client.get_container_client(container_name).list_blobs()

databases = [blob.name for blob in blob_list if blob.name.endswith("_index")]

# if blob_list:
#     blob_info = [{"name": blob.name, "size": blob.size} for blob in blob_list][:10]
#     print("blob_info:", blob_info)
print("databases:", databases)
