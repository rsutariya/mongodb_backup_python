# mongodb_backup_python

Here is a script that facilitates backup of MongoDB from an ec2 instance to an s3 bucket. It contains two scripts.

  - initBackup.py : For initialising the backup process
  - execBackup.py(utility for initBackup) : For execution of the backup process 


# usage
  - SSH into your s3 bucket and clone this repo by running "git clone "https://github.com/rsutariya/mongodb_backup_python.git" in the directory where you have your mongo db.
  - Run initBackup.py by "python3 initBackup.py --minutes <After how many minutes you want to take backup> --s3loc <name of the s3 bucket>" 

# dependancies 
- You will need boto3 library. Install it by "pip3 install boto3"

