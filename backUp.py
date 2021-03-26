import time
import os
import sys
import boto3
import schedule
from mongoDump import MongoDump

class Backup:
    
    def __init__(self, local_directory, s3Bucket, s3Path):
        self.local_directory = local_directory
        self.s3Bucket = s3Bucket
        self.s3Path = s3Path
        self.client = boto3.client("s3")
        self.dumper = MongoDump(port="27017", host="NA", username="NA", password="NA", outputDirectory="/home/ubuntu/test")
        self.foldersToUpload = []

    def cleaner():
        #task is to clean test after 24 hrs
        pass

    def findFoldersToUpload(self):
        self.foldersToUpload = []
        for root, dirs, files in os.walk(self.local_directory):
            for filename in files:
                print(filename)
                local_path = os.path.join(root, filename)
                relative_path = os.path.relpath(local_path, self.local_directory)
                s3_path = os.path.join(self.s3Path, relative_path)

                try:
                    print("In try block")
                    client.head_object(Bucket=self.s3Bucket, Key = s3_path)
            

                except:
                    self.foldersToUpload.append((local_path, s3_path))
            print("Folders to upload are")
            print(self.foldersToUpload)


    def uploadToS3(self):
            #self.dumper.takeDump()
            fols = self.findFoldersToUpload()            
            print(fols)
            print("Going to upload")
            for val in self.foldersToUpload:
                print("Uploading {0} to s3".format(val))

                self.client.upload_file(val[0], self.s3Bucket, val[1])

    def scheduledUpload(self,interval = 1):
        schedule.every(interval).hour.do(self.uploadToS3)
        while True:
            schedule.run_pending()
            time.sleep(1)



if __name__ == "__main__":
    backup = Backup(local_directory="/home/ubuntu/test", s3Bucket="backup.mongo.test", s3Path="Backup/")    
    #backup.scheduledUpload()
    backup.uploadToS3()

