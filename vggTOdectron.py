import skimage.io
import math
from itertools import chain
import numpy as np
import json
import os

def PolyArea(x,y):
    return 0.5*np.abs(np.dot(x,np.roll(y,1))-np.dot(y,np.roll(x,1)))

def vgg_to_coco(dataset_dir, vgg_path: str, outfile: str=None, class_keyword: str = "label", classes=[]):
    with open(vgg_path) as f:
        vgg = json.load(f)

    dataset_dicts = []
    for i in vgg:
        v = vgg[i]
        print(v['filename'])
        filename = os.path.join(dataset_dir, v['filename'])
        image = skimage.io.imread(filename)
        height, width = image.shape[:2]  
        annotations = []
        for j in v["regions"]:
            classes_id= j['region_attributes'][class_keyword]
            px = j["shape_attributes"]["all_points_x"]
            py= j["shape_attributes"]["all_points_y"]
            poly = [(x, y) for x, y in zip(px, py)] # poly for segmentation
            poly = [p for x in poly for p in x]
            
            obj = {
                "bbox": [min(px), min(py), max(px), max(py)],
                "bbox_mode": 0,
                "segmentation": [poly],
                "category_id": classes.index(classes_id),
                "iscrowd": 0
            }
            annotations.append(obj)
            
            
        record = {
            "file_name": filename,
            "height": height,
            "width": width,
            "annotations": annotations
        }
        print(record)
        dataset_dicts.append(record)
    return  dataset_dicts
    # record = {}
    # for i,v in enumerate(vgg.values()):
    #     filename = os.path.join(dataset_dir, v['filename'])
    #     image = skimage.io.imread(filename)
    #     height, width = image.shape[:2]  
    #     record["file_name"] = filename
    #     record["height"] = height
    #     record["width"] = width

        # classes_id = v["regions"]["region_attributes"]
        # annotations = []
        # for j, r in enumerate(v["regions"]):
        #     px = r["shape_attributes"]["all_points_x"]
        #     py= r["shape_attributes"]["all_points_y"]
        #     poly = [(x, y) for x, y in zip(px, py)] # poly for segmentation
        #     poly = [p for x in poly for p in x]
            
        #     obj = {
        #         "bbox": [np.min(px), np.min(py), np.max(px), np.max(py)],
        #         "bbox_mode": 0,
        #         "segmentation": [poly],
        #         "category_id": classes.index(classes_id),
        #         "iscrowd": 0
        #     }
        #     annotations.append(obj)
        # return classes_id

    # coco = {
    #     "images": images_info,
    #     "categories": categories,
    #     "annotations": annotations
    #     }
    # if outfile is None:
    #     outfile = vgg_path.replace(".json", "_coco.json")
    # with open(outfile, "w") as f:
    #     json.dump(coco, f)
        
dataset_dir = 'C:/Users/User/Documents/testLinux/sawit/train'
vgg_path= 'C:/Users/User/Documents/testLinux/sawit/train/via_region_data.json '
outfile='C:/Users/User/Documents/testLinux/train_dect.json'
class_keyword = "oilpalm"
classes = ['unripe', 'underripe','ripe','overripe']
y=vgg_to_coco(dataset_dir,vgg_path,outfile,class_keyword,classes)
print(y)
y = json.dumps(y)
y = json.loads(y)
filename = 'C:/Users/User/Documents/testLinux/sawittest2.json'          #use the file extension .json
with open(filename, 'w') as file_object:  #open the file in write mode
  json.dump(y, file_object,)