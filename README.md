# mongodb_backup_python

Here is a script that facilitates backup of MongoDB from an ec2 instance to an s3 bucket. It contains two scripts.

  - initBackup.py : For initialising the backup process
  - execBackup.py(utility for initBackup) : For execution of the backup process 


# usage
  - SSH into your s3 bucket and clone this repo by running "git clone "https://github.com/rsutariya/mongodb_backup_python.git" in the directory where you have your mongo db.
## make a systemd service
  -- chage directory to /home/ubuntu/.config/systemd/user
  -- copy the file backup_servic.service there.
  -- Start the service by "systemctl --backup_service"

# dependancies 
- You will need boto3 library. Install it by "pip3 install boto3"

