from fastapi import FastAPI
from fastapi.responses import HTMLResponse
# import logging

# import faiss
# import numpy as np
# import io
# from fastapi import FastAPI, File, UploadFile, Request, HTTPException 
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi.responses import FileResponse
# from starlette.responses import JSONResponse
# from azure.storage.blob import BlobServiceClient
# import os
# from dotenv import load_dotenv
# import openai
# from docx import Document
# from docx.shared import Pt
# from docx.enum.text import WD_PARAGRAPH_ALIGNMENT

# import pdb
# from datetime import datetime
# import re
# import requests

# #from BasePrompts import eti_prompt


# #from BlogExamples import blog_examples, recent_example, stamos_example, disney_example, long_form_examples, sector_example
# import PyPDF2


# def list_all_blobs_in_container(container_client):
#     print(f"Listing all blobs in the container: {container_client.container_name}")
#     blobs = container_client.list_blobs()
#     all_blobs = []
#     for blob in blobs:
#         print(f"Found blob: {blob.name}")
#         all_blobs.append(blob.name)
    
#     #pdb.set_trace()
#     return all_blobs



# logging.basicConfig(level=logging.DEBUG)


# app = FastAPI()

# openai.api_key = os.getenv('OPENAI_API_KEY')
# account_key = os.getenv('AZURE_STORAGE_ACCOUNT_KEY')
# account_name = "yorkvilleworks9016610742"

# # Form the connection string
# connection_string = f"DefaultEndpointsProtocol=https;AccountName={account_name};AccountKey={account_key};EndpointSuffix=core.windows.net"

# # Create a BlobServiceClient
# print("Creating BlobServiceClient...")
# #blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# container_name = "uploaded-files"

# container_client = blob_service_client.get_container_client(container_name)

# #blobs_in_container = list_all_blobs_in_container(container_client)

# # client = openai.OpenAI(
# #     api_key=oopenai.api_key,
# # )

# app = FastAPI()

# # Configure CORS
# origins = [
#     "http://localhost:3000",  # React dev server
#     "https://askyorkville-c3ckc8hgh4hzajeu.eastus-01.azurewebsites.net"  # For HTTPS
# ]

# app.add_middleware(
#     CORSMiddleware,
#     #allow_origins=origins,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# print('GOT CORS CONFIGURED SUCCESSFULLY')


# chunks_storage = {}  # {index: chunk_text}

# #promptTemplates = ["Ad Hoc Query", "Tear Sheet", "Long Form", "SuperLong", "One Page Current Events"]



# def get_chunk_by_index(idx):
#     return chunks_storage.get(idx, "")

# @app.exception_handler(413)
# async def request_entity_too_large_handler(request: Request, exc: Exception):
#     return JSONResponse(
#         status_code=413,
#         content={"message": "Payload too large"},
#     )

# # Increase the maximum payload size
# from fastapi.middleware.trustedhost import TrustedHostMiddleware
# app.add_middleware(
#     TrustedHostMiddleware,
#     allowed_hosts=["*"],
# )

# # Initialize Faiss index
# d = 1536  # Dimension of the embeddings
# index = faiss.IndexFlatL2(d)

# # Initialize Azure Blob Storage
# account_name = "yorkvilleworks9016610742"

# # Form the connection string
# connection_string = f"DefaultEndpointsProtocol=https;AccountName={account_name};AccountKey={account_key};EndpointSuffix=core.windows.net"

# # Create a BlobServiceClient
# print("Creating BlobServiceClient...")
# #blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# container_name = "uploaded-files"

# container_client = blob_service_client.get_container_client(container_name)

# #blobs_in_container = list_all_blobs_in_container(container_client)



# try:
#     # Initialize the BlobServiceClient
    
#     blob_list = blob_service_client.get_container_client(container_name).list_blobs()
#     #container_client = blob_service_client.get_container_client(container_name)

#     #blobs_in_container = list_all_blobs_in_container(container_client)

#     databases = [blob.name for blob in blob_list if blob.name.endswith("_index")]
   
# except Exception as e:
#     blob_list = None
#     error_message = str(e)



# @app.get("/api/azure-sdk-versions")
# async def get_azure_sdk_versions():
#     azure_packages = [p for p in pkg_resources.working_set if 'azure' in p.project_name]
#     versions = {p.project_name: p.version for p in azure_packages}
#     return versions


# # @app.get("/api/check-blob-service")
# # async def check_blob_service():
# #     #if blob_service_client:
# #     if blob_list:
# #         #return JSONResponse(content={"status": "success", "message": "BlobServiceClient is initialized successfully."})
# #         return {"message": "we do seem to have blob_list"}
# #         #return blob_list
# #     else:
# #         return JSONResponse(content={"status": "error", "message": f"BlobServiceClient initialization failed: {error_message}"})

# @app.get("/api/check-blob-service")
# async def check_blob_service():
#     #if blob_list:
#     if blobs_in_container:
#         blob_info = [{"name": blob.name, "size": blob.size} for blob in blobs_in_container][:10]
#         return {"message": "we do seem to have blobs_in_container", "blob_info": blob_info}
#     else:
#         return {"status": "error", "message": f"BlobServiceClient initialization failed: {error_message}"}






# @app.get("/api/test")
# async def test_endpoint():
#     return {"message": "Hello from your FastAPI app!"}


# @app.get("/api/vector-databases")
# #@app.get("/vector-databases")
# async def list_vector_databases():
#     print("Databases being requested")


#     logging.debug("Databases being requested")
#     try:
#         blob_list = blob_service_client.get_container_client(container_name).list_blobs()
#         #databases = [blob.name for blob in blob_list if blob.name.endswith("_index")]
#         #logging.debug(f"Databases found: {databases}")
#         return blob_list
#         #return {"message": "got databases but can't return them"}

#     except Exception as e:
#         logging.error(f"Error occurred: {str(e)}")
#         raise HTTPException(status_code=500, detail="Internal Server Error")
    
#     # blob_list = blob_service_client.get_container_client(container_name).list_blobs()
#     # databases = [blob.name for blob in blob_list if blob.name.endswith("_index")]
#     # print("Databases found:", databases)
#     # return databases







@app.get("/", response_class=HTMLResponse)
def read_root():
    
    current_time = datetime.now().strftime("%A %I:%M %p")
    return """
    <html>
        <head>
            <title>Testing Azure WebAPP functionality</title>
            <style>
                body {
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    font-family: Arial, sans-serif;
                    background-color: #f0f0f0;
                }
                h1 {
                    font-size: 3em;
                    color: #333;
                }
            </style>
        </head>
      <body>
            <h1>Hello, World Again! from branch incr2. today is {current_time}</h1>
        </body>
    </html>
    """







# from fastapi import FastAPI
# from fastapi.responses import HTMLResponse

# app = FastAPI()

# @app.get("/", response_class=HTMLResponse)
# def read_root():
#     return """
#     <html>
#         <head>
#             <title>Hello World. Again!!!</title>
#             <style>
#                 body {
#                     display: flex;
#                     justify-content: center;
#                     align-items: center;
#                     height: 100vh;
#                     margin: 0;
#                     font-family: Arial, sans-serif;
#                     background-color: #f0f0f0;
#                 }
#                 h1 {
#                     font-size: 3em;
#                     color: #333;
#                 }
#             </style>
#         </head>
#         <body>
#             <h1>Hello, World! Again. Wednesday 8:30 pm</h1>
#         </body>
#    </html>
#    """
