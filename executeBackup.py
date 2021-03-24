import os
import sys
import time
import boto3
import schedule


interval_m = 1
outputs_dir = '/home/ubuntu/test/'

host = "NA"
port = "27017"

username = "NA"
password = "NA"

current_time = time.strftime("%d-%m-%Y-%H:%M")


def render_output_locations():
    return outputs_dir + "/" + current_time 

def run_backup():
  command = "mongodump"
  if host != 'NA':
    command += " --host " + host
  if port != '27017':
    command += " --port " + port
  if username != 'NA':
    command += " --username " + username
  if password != 'NA':
    command += " --password " + password
  
  command += " --out " + render_output_locations()
  
  os.system(command)



def main():

    print("mongo backup progress started")
    print("I will backup your mongo db every {0} minutes".format(interval_m))

    run_backup()


    local_directory, bucket, destination = './test' , 'backup.mongo.test', 'Backup/'
    client = boto3.client('s3')
# s3.upload_file(Bucket='backup.mongo.test',Key='Backup/',Filename='test/')
    for root, dirs, files in os.walk(local_directory):

        for filename in files:

            local_path = os.path.join(root, filename)

            relative_path = os.path.relpath(local_path, local_directory)
            s3_path = os.path.join(destination, relative_path)


            print ("Searching {0} in {1}".format(s3_path, bucket))
            try:
                client.head_object(Bucket=bucket, Key=s3_path)
                #:print ("Path found on S3! Skipping {}..." .format(s3_path))

            except:
                print( "Uploading {}..." .format(s3_path))
                client.upload_file(local_path, bucket, s3_path)

                print("Done")


if __name__ == "__main__":  
    main()
