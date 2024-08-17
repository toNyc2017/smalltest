import os
import hashlib

# Retrieve the environment variable
secret_value = os.getenv('AZURE_STORAGE_ACCOUNT_PASSWORD')

dummy_string = "does this work?"

print(dummy_string)


if secret_value:
    # Perform an operation using the secret
    hashed_value = hashlib.sha256(secret_value.encode()).hexdigest()
    print(f"Secret is set and its hash is: {hashed_value}")
else:
    print("Secret is not set.")
