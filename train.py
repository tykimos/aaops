# train.py arch/ARC000001_train.py train/TRD000001_x.npy train/TRD000001_y.npy model/MDL000001.h5

# import

import sys
import os

# argv

arch_fn  = sys.argv[1] 
train_x_fn = sys.argv[2]
train_y_fn = sys.argv[3]
model_fn = sys.argv[4]

cmd = "python {0} {1} {2} {3}".format(arch_fn, train_x_fn, train_y_fn, model_fn)
print(cmd)
os.system(cmd)