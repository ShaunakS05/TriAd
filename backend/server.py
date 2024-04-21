from fastapi import FastAPI, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi import UploadFile
from fastapi.responses import JSONResponse
import os
import shutil

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origin=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

@app.get("/")
def home():
    return {"Data", "Test"}

@app.post("/upload-images")
async def upload_images(file_upload: UploadFile):
    file_path = os.path.join("uploads", file_upload.filename)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file_upload.file, buffer)