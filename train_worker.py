'''
python train_workder.py wo/train/
    train_TSK000001_ARC000001_TRD000001_MDL000001.wo
    train.py arch/ARC000001_train.py train/TRD000001_x.npy train/TRD000001_y.npy model/MDL000001.h5
    train_record.py task/TSK000001_model.csv ARC000001 TRD000001 MDL000001
        task/TSK000001_model.csv
            2020-12-06 19:37:43.802650, ARC000001, TRD000001, MDL000001
'''

# import

import sys
import time
import datetime
import os

# argv

wait_dir = "ops/wo/train/wait/"
running_dir = "ops/wo/train/running/"
success_dir = "ops/wo/train/success/"
fail_dir = "ops/wo/train/fail/"

while True:
    print("check " + str(datetime.datetime.now()))
    print("dir " + wait_dir)
    
    files = os.listdir(wait_dir)

    for filename in files:
        print(filename) # ['train_TSK000001_ARC000001_TRD000001_MDL000001.wo']
        arg = filename.split(".")[0].split("_")

        os.rename(wait_dir+filename, running_dir+filename)
        print("move wo to running. ", filename)

        # python train.py asset/arch/ARC000001_train.py asset/train/TRD000001_x.npy asset/train/TRD000001_y.npy asset/model/MDL000001.h5
        cmd = "python train.py asset/arch/{0}_train.py asset/train/{1}_x.npy asset/train/{2}_y.npy asset/model/{3}.h5".format(arg[2], arg[3], arg[3], arg[4])
        print(cmd)
        os.system(cmd)

        # python train_record.py ops/record/TSK000001_model.csv ARC000001 TRD000001 MDL000001
        cmd = "python train_record.py ops/record/{0}_model.csv {1} {2} {3}".format(arg[1], arg[2], arg[3], arg[4])
        print(cmd)
        os.system(cmd)

        os.rename(running_dir+filename, success_dir+filename)
        print("move wo to success. ", filename)

    time.sleep(3)        
