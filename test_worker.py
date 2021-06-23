'''
python test_worker.py wo/test/
    test_TSK000001_ARC000001_MDL000001_TST000001_SCR000001.wo
    test.py arch/ARC000001_test.py model/MDL000001.h5 test/TST000001_x.npy test/TST000001_y.npy score/SCR000001.txt
    test_record.py task/TSK000001_score.csv MDL000001 TST000001 score/SCR000001.txt
        task/TSK000001_score.csv
            2020-12-06 19:07:28.350469, MDL000001, TST000001, score/SCR000001.txt, 0.10050000250339508
'''

# import

import sys
import time
import datetime
import os

# argv

wait_dir = "ops/wo/test/wait/"
running_dir = "ops/wo/test/running/"
success_dir = "ops/wo/test/success/"
fail_dir = "ops/wo/test/fail/"

while True:
    print("check " + str(datetime.datetime.now()))
    print("dir " + wait_dir)
    
    files = os.listdir(wait_dir)

    for filename in files:
        print(filename) # ['test_TSK000001_ARC000001_MDL000001_TST000001_SCR000001.wo']
        arg = filename.split(".")[0].split("_")

        os.rename(wait_dir+filename, running_dir+filename)
        print("move wo to running. ", filename)

        # python test.py asset/arch/ARC000001_test.py asset/model/MDL000001.h5 asset/test/TST000001_x.npy asset/test/TST000001_y.npy asset/score/SCR000001.txt
        cmd = "python test.py asset/arch/{0}_test.py asset/model/{1}.h5 asset/test/{2}_x.npy asset/test/{3}_y.npy asset/score/{4}.txt".format(arg[2], arg[3], arg[4], arg[4], arg[5])
        print(cmd)
        os.system(cmd)

        # python test_record.py ops/record/TSK000001_score.csv MDL000001 TST000001 asset/score/SCR000001.txt
        cmd = "python test_record.py ops/record/{0}_score.csv {1} {2} asset/score/{3}.txt".format(arg[1], arg[3], arg[4], arg[5])
        print(cmd)
        os.system(cmd)

        os.rename(running_dir+filename, success_dir+filename)
        print("move wo to success. ", filename)

    time.sleep(3)        
