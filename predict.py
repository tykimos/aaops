# predict.py arch/ARC000001_predict.py model/MDL000001.h5 predict/PRD000001_x.npy out/PRD000001_yhat.npy

# import

import sys
import os

# argv

arch_fn  = sys.argv[1] 
model_fn = sys.argv[2]
predict_fn = sys.argv[3]
out_fn = sys.argv[4]

cmd = "python {0} {1} {2} {3}".format(arch_fn, model_fn, predict_fn, out_fn)
print(cmd)
os.system(cmd)