import os
import skimage.io
import numpy as np
from itertools import chain
import math
import json

def PolyArea(x,y):
    return float(0.5*np.abs(np.dot(x,np.roll(y,1))-np.dot(y,np.roll(x,1))))


class_keyword = "oilpalm"
path = "C:/Users/User/Desktop/segmentation/sawit"
dir_list = os.listdir(path)
class_list = ['overripe', 'ripe', 'underripe', 'unripe']
category_ids_dict = {c: i for i, c in enumerate(class_list, 0)}
categories = [{"supercategory": class_keyword, "id": v, "name": k} for k, v in category_ids_dict.items()]
print(dir_list)
i=0
for folder in dir_list:
    images_ids_dict = {}
    images_info = []
    annotations = []
    img_list = os.listdir(os.path.join(path, folder))
    for v in img_list:
        images_ids_dict[v] = i
        image = skimage.io.imread(os.path.join(path,folder,v))
        height, width = image.shape[:2] 
        images_info.append({"file_name": v, "id": i, "width": width, "height": height})
        point = [[117,203],[48,199],[10,165],[13,122],[48,57],[113,4],[177,58],[216,121],[218,169],[179,191],[117,203]]
        x=[]
        y=[]
        for p in point:
            x.append(float(p[0]))
            y.append(float(p[1]))
            
        annotations.append({
                "segmentation": [list(chain.from_iterable(zip(x, y)))],
                "area": PolyArea(x, y),
                "bbox": [float(min(x)), float(min(y)), float(max(x)-min(x)), float(max(y)-min(y))],
                "image_id": images_ids_dict[v],
                "category_id": category_ids_dict[v.split('_')[0]],
                "id": int(i),
                "iscrowd": 0
                })
        i+=1
    coco = {
        "images": images_info,
        "categories": categories,
        "annotations": annotations
        }
    print(coco)

    with open(os.path.join(path,folder,str(folder)+'_annotation.json'), 'w') as f:
        json.dump(coco, f)