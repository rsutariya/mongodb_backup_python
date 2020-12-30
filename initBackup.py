import os
import sys
import time
#import boto3
import argparse

parser = argparse.ArgumentParser(description= "For backing up mongodb from ec2 to s3")

parser.add_argument("--minutes", metavar="m", type=int, help="Inteval in mins before backup")

parser.add_argument("--s3loc", metavar="s", type=str, help="Destination s3 bucket")

args = parser.parse_args()



while 1:
    if (time.time() % (args.minutes*60) == 0):
        print("One minute passed, time to backup")
        os.system("python3 testExecBackup.py")
    else:
        continue