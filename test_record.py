#  test_record.py task/TSK000001_score.csv MDL000001 TST000001 score/SCR000001.txt
#        task/TSK000001_score.csv
#            timestamp MDL000001 TST000001 score/SCR000001.txt value

# import

import sys
import datetime

# argv

task_score_fn  = sys.argv[1] 
model_name = sys.argv[2]
test_name = sys.argv[3]
score_fn = sys.argv[4]

# get score

f = open(score_fn)
score_value = f.readline()
f.close()

# record score 

f = open(task_score_fn, 'at')
record = "{0}, {1}, {2}, {3}, {4}\n".format(datetime.datetime.now(), model_name, test_name, score_fn, score_value)
f.write(record)
f.close()