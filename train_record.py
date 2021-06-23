#  train_record.py task/TSK000001_model.csv ARC000001 TRD000001 MDL000001
#        task/TSK000001_model.csv
#            timestamp ARC000001 TRD000001 MDL000001

# import

import sys
import datetime

# argv

task_model_fn = sys.argv[1]
arch_name = sys.argv[2]
train_name = sys.argv[3]
model_name = sys.argv[4]

# record score 

f = open(task_model_fn, 'at')
record = "{0}, {1}, {2}, {3}\n".format(datetime.datetime.now(), arch_name, train_name, model_name)
f.write(record)
f.close()