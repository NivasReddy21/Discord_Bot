import os

cur_dir = os.curdir
list1 = os.listdir(cur_dir)
imgs = []

def create_list():
    for i in list1:
        
        if i.endswith('.jpg') or i.endswith('.jpeg'):
            imgs.append(i)

    return imgs
