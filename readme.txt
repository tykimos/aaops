Kt media

train_wf.py
      7분에 한 번
      traingen_wogen.py
              task별 train셋 정보
      task별 arch셋 정보
      task_train열어서 model없으면 아래 생성
      train_wogen.py

test_wf.py
      3분에 한번
      testgen_wogen.py
              task별 test셋 정보
      task_model정보 가지고온뒤
      task_score열어서 score없으면 아래 생성
      test_wogen.py

predict_wf.py
      30초에 한 번
      predictgen_wogen.py
      task별 test셋 정보 열어서 가장최신 test셋 정보
       task_score열어서 해당 test셋에 가장 높은 score의 모델 정보 가지고 오기
      predict_wogen.py

task id
TSK000001

train dataset id
TRD000001_x.npy
TRD000001_y.npy

test dataset id
TST000001_x.npy
TST000001_y.npy

arch id
ARC000001_predict.py
ARC000001_train.py
ARC000001_test.py

model id
MDL000001

MDL000001,TSK000001,TRD000001,ARC000001
MDL000002,TSK000001,TRD000001,ARC000002
MDL000003,TSK000001,TRD000002,ARC000001

score id
SCR000001.txt

SCR000001,TSK000001,TST000001,MDL000001,score
SCR000002,TSK000001,TST000001,MDL000002,score
SCR000003,TSK000001,TST000002,MDL000003,score

predict dataset id
PDT000001_x.npy
PDT000001_y.npy

predict out dataset id

PDT000001_yhat.npy

wo

traindsgen 
testdsgen
predictdsgen

train TSK000001 TRD000001 ARC000001 >> MDL000001
train TSK000001 TRD000001 ARC000002 >> MDL000002
train TSK000001 TRD000002 ARC000001 >> MDL000003

test TSK000001 TST000001 MDL000001 >> SCR000001
test TSK000001 TST000001 MDL000002 >> SCR000002
test TSK000001 TST000002 MDL000003 >> SCR000003


predict TSK000001 MDL000001 PRD000001


wo

python traingen_workder.py wo/traingen/

    traingen 
        wait
        running
        success
        fail

traingen_TSK000001_TRD000001.wo
    traingen.py gen/TSK000001_train.py train/TRD000001_x.npy train/TRD000001_y.npy

python testgen_workder.py wo/testgen/

    testgen
        wait
        running
        success
        fail

testgen_TSK000001_TST000001.wo
    testgen.py gen/TSK000001_test.py test/TST000001_x.npy test/TST000001_y.npy

python predictgen_workder.py wo/predictgen/

    predictgen
        wait
        running
        success
        fail

predictgen_TSK000001_PRD000001.wo
    predictgen.py gen/TSK000001_predict.py predict/PRD000001_x.npy

python train_workder.py wo/train/

    train
        wait
        running
        success
        fail

train_TSK000001_ARC000001_TRD000001_MDL000001.wo
    python train.py arch/ARC000001_train.py train/TRD000001_x.npy train/TRD000001_y.npy model/MDL000001.h5
    python train_record.py task/TSK000001_model.csv ARC000001 TRD000001 MDL000001
        task/TSK000001_model.csv
            2020-12-06 19:37:43.802650, ARC000001, TRD000001, MDL000001

python test_worker.py wo/test/

test
    wait
    running
    success
    fail

test_TSK000001_ARC000001_MDL000001_TST000001_SCR000001.wo
    python test.py arch/ARC000001_test.py model/MDL000001.h5 test/TST000001_x.npy test/TST000001_y.npy score/SCR000001.txt
    python test_record.py task/TSK000001_score.csv MDL000001 TST000001 score/SCR000001.txt
        task/TSK000001_score.csv
            2020-12-06 19:07:28.350469, MDL000001, TST000001, score/SCR000001.txt, 0.10050000250339508

python predict_workder.py wo/predict/

predict
    wait
    running
    success
    fail

predcit_TSK000001_ARC000001_MDL000001_PRD000001.wo
    python predict.py arch/ARC000001_predict.py model/MDL000001.h5 predict/PRD000001_x.npy out/PRD000001_yhat.npy
    python predict_record.py task/TSK000001_predict.csv MDL000001 out/PRD000001_yhat.npy
        task/TSK000001_predict.csv
            2020-12-06 19:30:56.166444, MDL000001, out/PRD000001_yhat.npy, [[0.100