'''
python traingen_worker.py wo/traingen/
    traingen_TSK000001_TRD000001.wo
        traingen.py gen/TSK000001_train.py train/TRD000001_x.npy train/TRD000001_y.npy
'''

def get_task_id_list():
    task_id_list = os.listdir("id/task")
    for task_id in task_id_list:
        task_id = task_id.split(".")[0]

def get_arch_id_list(task_id):
    arch_id_list = np.loadtxt('ops/record/' +  task_id + '_arch.csv')
    return arch_id_list

def get_train_id_list(task_id):
    train_id_list = np.loadtxt('ops/record/' +  task_id + '_train.csv')
    return train_id_list    

def gen_new_id(base_path):

    files = os.listdir(base_path)
    files = files.sort(key=lambda f: int(filter(str.isdigit, f)), reserve=True)
    curr_id = files[0]
    next_id = "{0}{1}".format(curr_id[0:3], int(curr_id[3:])+1)
    f = open(base_path + "/" + next_id + ".id", w)
    f.close()
    return next_id

def create_traingen_wo():        
    task_id_list = os.listdir("id/task")
    
    for filename in files:
        print(filename) # TSK000001.id
        task_id = filename.split(".")[0]
        train_id = get_next_id(id_dir+"train")
        fp = open(id_dir+"train/"+train_id+".id", "w") # TRD000001.id
        fp.close()
        new_wo = "traingen_{0}_{1}".format(task_id, train_id)
        fp = open(wo_dir+"traingen_{0}_{1}.wo", task_id,train_id) # "traingen_TSK000001_TRD000001.wo"
        fp.close()
    
def create_train_wo():
    task_id_list = os.listdir("id/task")

    for task_id in task_id_list:

        arch_id_list = get_arch_id_list(task_id)
        train_id_list = get_train_id_list(task_id)

        arc_train_dic = {}

        for arch_id in arch_id_list:
            arc_train_dic[arch_id] = {}
            for train_id in train_id_list:
                arch_train_dic[arch_id][train_id] = 0

        model_record_list = np.loadtxt('ops/record/' +  task_id + '_model.csv')

        for model_record in model_record_list:
            arch_train_dic[model_record[1]][model_record[2]] = 1
            # 2020-12-06 23:07:07.318792, ARC000001, TRD000002, MDL000003

        for arch_id in arch_id_list:
            for train_id in train_id_list:
                if arch_train_dic[arch_id][train_id] == 0:
                    model_id = gen_new_id('id/model')
                    # train_TSK000001_ARC000001_TRD000001_MDL000001.wo
                    wo_name = "wo/train/wait/train_{0}_{1}_{2}_{3}.wo".format(task_id, arch_id, train_id, model_id)
                    fp = open(wo_name, "w")
                    fp.close()


TRAINGEN_CHECK_PERIOD = 60 * 7
TRAIN_CHECK_PERIOD = 10

# import

import sys
import time
import datetime
import os
import subprocess

# argv

id_dir = sys.argv[1]
wo_dir = sys.argv[2]

traingen_base_time = time.time()
train_base_time = time.time()

while True:

    print("check " + str(datetime.datetime.now()))
    
    curr_time = time.time()

    remain_next_traingen = traingen_base_time - curr_time
    remain_next_train = train_base_time - curr_time

    print("remain time traingen:{0} train:{1}".format(remain_next_traingen,remain_next_train))

    if remain_next_traingen > TRAINGEN_CHECK_PERIOD:
        create_traingen_wo()
        traingen_base_time = curr_time

    if remain_next_train > TRAIN_CHECK_PERIOD:
        create_train_wo()
        train_base_time = curr_time

    time.sleep(3)