import skimage 
import math
from itertools import chain
import numpy as np
import json
import os

def PolyArea(x,y):
    return 0.5*np.abs(np.dot(x,np.roll(y,1))-np.dot(y,np.roll(x,1)))

def vgg_to_coco(dataset_dir, vgg_path: str, outfile: str=None, class_keyword: str = "label"):
    with open(vgg_path) as f:
        vgg = json.load(f)

    images_ids_dict = {}
    images_info = []
    for i,v in enumerate(vgg.values()):

        images_ids_dict[v["filename"]] = i
        image_path = os.path.join(dataset_dir, v['filename'])
        image = skimage.io.imread(image_path)
        height, width = image.shape[:2]  
        images_info.append({"file_name": v["filename"], "id": i, "width": width, "height": height})

    classes = {class_keyword} | {r["region_attributes"][class_keyword] for v in vgg.values() for r in v["regions"].values()
                             if class_keyword in r["region_attributes"]}
    category_ids_dict = {c: i for i, c in enumerate(classes, 1)}
    categories = [{"supercategory": class_keyword, "id": v, "name": k} for k, v in category_ids_dict.items()]
    annotations = []
    suffix_zeros = math.ceil(math.log10(len(vgg)))
    for i, v in enumerate(vgg.values()):
        for j, r in enumerate(v["regions"].values()):
            if class_keyword in r["region_attributes"]:
                x, y = r["shape_attributes"]["all_points_x"], r["shape_attributes"]["all_points_y"]
                annotations.append({
                    "segmentation": [list(chain.from_iterable(zip(x, y)))],
                    "area": PolyArea(x, y),
                    "bbox": [min(x), min(y), max(x)-min(x), max(y)-min(y)],
                    "image_id": images_ids_dict[v["filename"]],
                    "category_id": category_ids_dict[r["region_attributes"][class_keyword]],
                    "id": int(f"{i:0>{suffix_zeros}}{j:0>{suffix_zeros}}"),
                    "iscrowd": 0
                    })

    coco = {
        "images": images_info,
        "categories": categories,
        "annotations": annotations
        }
    if outfile is None:
        outfile = vgg_path.replace(".json", "_coco.json")
    with open(outfile, "w") as f:
        json.dump(coco, f)
        

vgg_to_coco("C:/Users/User/Downloads/dataset-20220124T045838Z-001/dataset", "C:/Users/User/Downloads/dataset-20220124T045838Z-001/dataset/train/via_region_data.json","C:/Users/User/Downloads/dataset-20220124T045838Z-001/dataset/train/via_region_data_coco.json")