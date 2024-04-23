import pymongo
import os
import gridfs

from pymongo import MongoClient

myclient = pymongo.MongoClient("mongodb+srv://bryanxiong:ooAdsV5zhmGfd8Gz@vrvid.5snicca.mongodb.net/?retryWrites=true&w=majority")

mydb = myclient["vrvid"]

mycol = mydb["vids"]

def mongo_conn():
    """create a connection"""
    try:
        return myclient.vids
    except Exception as err:
        print(f"Error in mongodb connection: {err}")


def upload_file(file_loc, file_name, fs):
    """upload file to mongodb"""
    with open(file_loc, 'rb') as file_data:
        data = file_data.read()

    # put file into mongodb
    fs.put(data, filename=file_name)
    print("Upload complete")


def download_file(download_loc, db, fs, file_name):
    """download file from mongodb"""
    data = db.vids.files.find_one({"filename": file_name})

    fs_id = data['_id']
    out_data = fs.get(fs_id).read()

    with open(download_loc, 'wb') as output:
        output.write(out_data)

    print("Download complete")


if __name__ == '__main__':
    file_name = "fish.mp4"
    file_loc = os.path.join(os.getcwd() + "/" + file_name)
    if not os.path.exists(os.getcwd() + "/Downloads"):
                    os.makedirs(os.getcwd() + "/Downloads")
    down_loc = os.path.join(os.getcwd() + "/Downloads/", file_name)

    db = mongo_conn()
    fs = gridfs.GridFS(db, collection="vids")

    # upload file
    upload_file(file_loc=file_loc, file_name=file_name, fs=fs)
    # download file
    # download_file(down_loc, db, fs, file_name)