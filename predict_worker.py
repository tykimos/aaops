'''
python predict_worker.py wo/predict/
    predcit_TSK000001_ARC000001_MDL000001_PRD000001.wo
    predict.py arch/ARC000001_predict.py model/MDL000001.h5 predict/PRD000001_x.npy out/PRD000001_yhat.npy
    predict_record.py task/TSK000001_predict.csv MDL000001 out/PRD000001_yhat.npy
        task/TSK000001_predict.csv
            2020-12-06 19:30:56.166444, MDL000001, out/PRD000001_yhat.npy, [[0.100
'''

# import

import sys
import time
import datetime
import os

# argv

wait_dir = "ops/wo/predict/wait/"
running_dir = "ops/wo/predict/running/"
success_dir = "ops/wo/predict/success/"
fail_dir = "ops/wo/predict/fail/"

while True:
    print("check " + str(datetime.datetime.now()))
    print("dir " + wait_dir)
    
    files = os.listdir(wait_dir)

    for filename in files:
        print(filename) # ['predcit_TSK000001_ARC000001_MDL000001_PRD000001.wo']
        arg = filename.split(".")[0].split("_")

        os.rename(wait_dir+filename, running_dir+filename)
        print("move wo to running. ", filename)

        # python predict.py asset/arch/ARC000001_predict.py asset/model/MDL000001.h5 ops/predict/PRD000001_x.npy ops/out/PRD000001_yhat.npy
        cmd = "python predict.py asset/arch/{0}_predict.py asset/model/{1}.h5 ops/predict/{2}_x.npy ops/out/{3}_yhat.npy".format(arg[2], arg[3], arg[4], arg[4])
        print(cmd)
        os.system(cmd)

        # python predict_record.py ops/record/TSK000001_predict.csv MDL000001 ops/out/PRD000001_yhat.npy
        cmd = "python predict_record.py ops/record/{0}_predict.csv {1} ops/out/{2}_yhat.npy".format(arg[1], arg[3], arg[4])
        print(cmd)
        os.system(cmd)

        os.rename(running_dir+filename, success_dir+filename)
        print("move wo to success. ", filename)

    time.sleep(3)        
