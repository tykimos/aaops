# python traingen.py gen/TSK000001_train.py train/TRD000001_x.npy train/TRD000001_y.npy

# import

import sys
import os

# argv

gen_fn  = sys.argv[1] 
train_x_fn = sys.argv[2]
train_y_fn = sys.argv[3]

cmd = "python {0} {1} {2}".format(gen_fn, train_x_fn, train_y_fn)
print(cmd)
os.system(cmd)