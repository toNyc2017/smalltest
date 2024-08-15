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
            <h1>Hello, World! Again. Thus 9:00 am incr2 branch</h1>
        </body>
    </html>
    """
