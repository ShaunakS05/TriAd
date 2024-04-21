from fastapi import FastAPI, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi import UploadFile
from fastapi.responses import JSONResponse
import os
import shutil

app = FastAPI()

origins =  [
    'http://localhost:3000'
]
app.add_middleware(
    CORSMiddleware, 
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.get("/")
def home():
    return {"Data": "Test"}

@app.post("/upload-images")
async def upload_images(video: UploadFile):
    contents = await video.read()
    print("hi")
    #file_path = os.path.join("uploads", video.filename)
    #os.makedirs(os.path.dirname(file_path), exist_ok=True)
    #with open(file_path, "wb") as buffer:
    #    shutil.copyfileobj(video.file, buffer)
    return True