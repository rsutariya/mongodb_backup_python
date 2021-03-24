import os
import sys
import time
import schedule 

def job():
        os.system("python3 execBackup.py")


if __name__ == "__main__":
    schedule.every(1).hour.do(job) #can work for mins as schedule.every(#mins).minutes.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)
