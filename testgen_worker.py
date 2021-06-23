'''
python testgen_workder.py wo/testgen/
    testgen_TSK000001_TST000001.wo
        testgen.py dsgen/TSK000001_test.py test/TST000001_x.npy test/TST000001_y.npy
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
        print(filename) # ['testgen_TSK000001_TST000001.wo']
        arg = filename.split(".")[0].split("_")

    
        os.rename(wait_dir+filename, running_dir+filename)
        print("move wo to running. ", filename)

        # python testgen.py gen/TSK000001_test.py test/TST000001_x.npy test/TST000001_y.npy
        cmd = "python testgen.py gen/{0}_test.py test/{1}_x.npy test/{2}_y.npy".format(arg[1], arg[2], arg[3])
        print(cmd)
        os.system(cmd)

        os.rename(running_dir+filename, success_dir+filename)
        print("move wo to success. ", filename)

    time.sleep(3)        
