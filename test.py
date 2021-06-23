# test.py arch/ARC000001_test.py model/MDL000001.h5 test/TST000001_x.npy test/TST000001_y.npy score/SCR000001.txt

# import

import sys
import os

# argv

arch_fn  = sys.argv[1] 
model_fn = sys.argv[2]
test_x_fn = sys.argv[3]
test_y_fn = sys.argv[4]
score_fn = sys.argv[5]

cmd = "python {0} {1} {2} {3} {4}".format(arch_fn, model_fn, test_x_fn, test_y_fn, score_fn)
print(cmd)
os.system(cmd)