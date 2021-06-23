'''
python traingen_worker.py wo/traingen/
    traingen_TSK000001_TRD000001.wo
        traingen.py gen/TSK000001_train.py train/TRD000001_x.npy train/TRD000001_y.npy
'''

# import

import sys
import time
import datetime
import os

# argv

base_dir = sys.argv[1]

wait_dir = base_dir + "wait/"
running_dir = base_dir + "running/"
success_dir = base_dir + "success/"
fail_dir = base_dir + "fail/"

while True:
    print("check " + str(datetime.datetime.now()))
    print("dir " + wait_dir)
    
    files = os.listdir(wait_dir)

    for filename in files:
        print(filename) # ['traingen_TSK000001_TRD000001.wo']
        arg = filename.split(".")[0].split("_")

        os.rename(wait_dir+filename, running_dir+filename)
        print("move wo to running. ", filename)

        # python traingen.py gen/TSK000001_train.py train/TRD000001_x.npy train/TRD000001_y.npy
        cmd = "python traingen.py gen/{0}_train.py train/{1}_x.npy train/{2}_y.npy".format(arg[1], arg[2], arg[2])
        print(cmd)
        os.system(cmd)

        os.rename(running_dir+filename, success_dir+filename)
        print("move wo to success. ", filename)

    time.sleep(3)        
