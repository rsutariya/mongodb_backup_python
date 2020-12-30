import os
import sys
import time
import boto3

while 1:
    if time.time() % 60 == 0:
        print("One minute passed, time to backup")
        os.system("python3 testExecBackup.py")
    else:
        continue