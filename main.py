from fastapi import FastAPI
from fastapi.responses import HTMLResponse

import faiss
import numpy as np
import io
from fastapi import FastAPI, File, UploadFile, Request, HTTPException 
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from starlette.responses import JSONResponse
from azure.storage.blob import BlobServiceClient
import os
from dotenv import load_dotenv
import openai
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT

import pdb
from datetime import datetime
import re
import requests

#from BasePrompts import eti_prompt


#from BlogExamples import blog_examples, recent_example, stamos_example, disney_example, long_form_examples, sector_example
import PyPDF2

app = FastAPI()


account_key = os.getenv('AZURE_STORAGE_ACCOUNT_KEY')

# client = openai.OpenAI(
#     api_key=oopenai.api_key,
# )

app = FastAPI()

# Configure CORS
origins = [
    "http://localhost:3000",  # React dev server
    "https://askyorkville-c3ckc8hgh4hzajeu.eastus-01.azurewebsites.net"  # For HTTPS
]

app.add_middleware(
    CORSMiddleware,
    #allow_origins=origins,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

print('GOT CORS CONFIGURED SUCCESSFULLY')


chunks_storage = {}  # {index: chunk_text}

#promptTemplates = ["Ad Hoc Query", "Tear Sheet", "Long Form", "SuperLong", "One Page Current Events"]



def get_chunk_by_index(idx):
    return chunks_storage.get(idx, "")

@app.exception_handler(413)
async def request_entity_too_large_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=413,
        content={"message": "Payload too large"},
    )

# Increase the maximum payload size
from fastapi.middleware.trustedhost import TrustedHostMiddleware
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["*"],
)

# Initialize Faiss index
d = 1536  # Dimension of the embeddings
index = faiss.IndexFlatL2(d)

# Initialize Azure Blob Storage
account_name = "yorkvilleworks9016610742"

# Form the connection string
connection_string = f"DefaultEndpointsProtocol=https;AccountName={account_name};AccountKey={account_key};EndpointSuffix=core.windows.net"

# Create a BlobServiceClient
print("Creating BlobServiceClient...")
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

container_name = "uploaded-files"




@app.get("/api/vector-databases")
#@app.get("/vector-databases")
async def list_vector_databases():
    print("Databases being requested")
    blob_list = blob_service_client.get_container_client(container_name).list_blobs()
    databases = [blob.name for blob in blob_list if blob.name.endswith("_index")]
    print("Databases found:", databases)
    return databases







@app.get("/", response_class=HTMLResponse)
def read_root():
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
            <h1>Hello, World! Again. Thus 9:30 am incr2 branch</h1>
        </body>
    </html>
    """
