#    predict_record.py task/TSK000001_predict.csv MDL000001 out/PRD000001_yhat.npy
#        task/TSK000001_predict.csv
#            timpstamp MDL000001 out/PRD000001_yhat.txt value


# import

import sys
import datetime
import numpy as np

# argv

predict_record_fn  = sys.argv[1] 
model_name = sys.argv[2]
predict_out_fn = sys.argv[3]

# get predict

predict_value = np.loadtxt(predict_out_fn)

# record predict 

f = open(predict_record_fn, 'at')
record = "{0}, {1}, {2}, {3}\n".format(datetime.datetime.now(), model_name, predict_out_fn, predict_value.tolist())
f.write(record)
f.close()