import os
import pathlib
import shutil
import pandas as pd
import json

df = pd.read_csv('awe/test.txt', delimiter=' ', header=None)
test_idx = df.values[0]
val_idx = df.values[1]

# select the folder you want to prepare
# folder = '/identity'
folder = '/ethnicity'
# folder = '/gender'


for dir in os.listdir('awe'):
    if os.path.isdir(os.path.join('./awe', dir)):
        annot_path = f'awe/{dir}/annotations.json'
        with open(annot_path, 'r') as j:
            annot = json.loads(j.read())
        if folder in ['/identity', '/small']:
            id = dir
        else:
            id = annot[folder[1:]]
        pathlib.Path(f'data{folder}/val/{id}').mkdir(parents=True, exist_ok=True)
        pathlib.Path(f'data{folder}/train/{id}').mkdir(parents=True, exist_ok=True)
        pathlib.Path(f'data{folder}/test/{id}').mkdir(parents=True, exist_ok=True)
        for file in os.listdir(f'awe/{dir}'):
            photo, e = file.split('.')
            if e == 'png':
                if (int(dir) - 1) * 10 + int(photo) in test_idx:
                    shutil.copy(f'awe/{dir}/{file}', f'data{folder}/test/{id}/{dir}_{file}')
                elif (int(dir) - 1) * 10 + int(photo) in val_idx:
                    shutil.copy(f'awe/{dir}/{file}', f'data{folder}/val/{id}/{dir}_{file}')
                else:
                    shutil.copy(f'awe/{dir}/{file}', f'data{folder}/train/{id}/{dir}_{file}')


