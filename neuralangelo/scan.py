import datetime
import time
import pymongo
import os
import gridfs

from datetime import timedelta
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

def scan_database():
    # Connect to MongoDB
    client = pymongo.MongoClient("mongodb+srv://bryanxiong:ooAdsV5zhmGfd8Gz@vrvid.5snicca.mongodb.net/?retryWrites=true&w=majority")
    db = client.vids
    lastScan = datetime.datetime.now() + timedelta(hours=4)
    
    # Main loop to scan for updates
    while True:
        try:
            # Perform your query to check for updates
            # For example, you could check for new documents added after the last scan

            # Wait for 15 seconds before the next scan
            print("Sleeping for 15 seconds")
            time.sleep(15)

            files = db.vids.files.find({'uploadDate': {'$gt': lastScan}})
            fs = gridfs.GridFS(db, collection="vids")
            
            # Process files
            for file in files:
                print("File found")
                fs_id = file['_id']
                # export the video
                file_name = str(fs_id) + ".mp4"
                if not os.path.exists(os.getcwd() + "/Downloads"):
                    os.makedirs(os.getcwd() + "/Downloads")
                down_loc = os.path.join(os.getcwd() + "/Downloads/", file_name)

                out_data = fs.get(fs_id).read()

                with open(down_loc, 'wb') as output:
                    output.write(out_data)
            
            # Update the last scan timestamp to the current time
            lastScan = datetime.datetime.now() + timedelta(hours=4)
            
        except ServerSelectionTimeoutError:
            # If server selection timeout occurs, log the error and retry after a delay
            print("Server selection timeout. Retrying in 10 seconds...")
            time.sleep(10)

if __name__ == "__main__":
    scan_database()