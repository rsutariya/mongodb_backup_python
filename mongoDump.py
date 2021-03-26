import os
import sys
import time 
import boto3
import schedule

# TO do: Implement a parent class for this one and make two child classes each for mongo and sql



class MongoDump:
    def __init__(self,port, host, username, password, outputDirectory):
        self.port = port
        self.host = host        
        self.creds = {
                "username" : username,
                "password" : password
                }

        self.outputDirectory = outputDirectory
        self.outputLocation = self.outputDirectory + "/" + time.strftime("%d-%m-%Y-%H:%M")
        self.command = ""
  

    def takeDump(self):
        self.command = "mongodump "
        
        if self.host != "NA":
            self.command += "--host " + host

        if self.port != "27017":
            self.command += "--port " + port

        if self.creds["username"] != "NA":
            self.command += "--username" + creds["username"]

        if self.creds["password"] != "NA":
            self.command += "--password" + creds["password"]

        self.command += "--out " + self.outputLocation

        os.system(self.command)



if __name__ == "__main__":

    dumper = MongoDump(port="27017", host="NA", username="NA", password="NA", outputDirectory="/home/ubuntu/test")
    
    dumper.takeDump()
