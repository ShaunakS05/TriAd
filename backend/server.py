from fastapi import FastAPI, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi import UploadFile
from fastapi.responses import JSONResponse
import os
import shutil
import pymongo
import os
import gridfs

from pymongo import MongoClient

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
    #contents = await video.read()
    #print("hi")
    #file_path = os.path.join("uploads", video.filename)
    #os.makedirs(os.path.dirname(file_path), exist_ok=True)
    #with open(file_path, "wb") as buffer:
    #    shutil.copyfileobj(video.file, buffer)
    #return True

    file_path = os.path.join("uploads", video.filename)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "wb") as buffer:
           shutil.copyfileobj(video.file, buffer) 

    myclient = pymongo.MongoClient("mongodb+srv://bryanxiong:ooAdsV5zhmGfd8Gz@vrcard.keif8ak.mongodb.net/?retryWrites=true&w=majority&appName=vrcard")
    mydb = myclient["vrvid"]
    mycol = mydb["vids"]

    file_name = video.filename
    file_loc = os.path.join(os.getcwd() + "\\uploads\\" + file_name)
    if not os.path.exists(os.getcwd() + "/Downloads"):
                    os.makedirs(os.getcwd() + "/Downloads")
    down_loc = os.path.join(os.getcwd() + "/Downloads/", file_name)

    db = myclient.vids
    fs = gridfs.GridFS(db, collection="vids")

    with open(file_loc, 'rb') as file_data:
        data = file_data.read()

    # put file into mongodb
    fs.put(data, filename=file_name)
    print("Upload complete")
    return True
    
