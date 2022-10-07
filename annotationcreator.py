import os
import skimage.io
import numpy as np
from itertools import chain
import math
import json

def PolyArea(x,y):
    return 0.5*np.abs(np.dot(x,np.roll(y,1))-np.dot(y,np.roll(x,1)))


class_keyword = "oilpalm"
path = "C:/Users/User/Desktop/synthetic_dataset"
dir_list = os.listdir(path)
category_ids_dict = {c: i for i, c in enumerate(dir_list, 1)}
categories = [{"supercategory": class_keyword, "id": v, "name": k} for k, v in category_ids_dict.items()]

filename=[]
for i in dir_list:
    img_list = os.listdir(os.path.join(path, i))
    for j in img_list:
        filename.append(os.path.join(path,i,j))


images_ids_dict = {}
images_info = []
for i,v in enumerate(filename):
    images_ids_dict[v.split('\\')[-1]] = i
    image = skimage.io.imread(v)
    height, width = image.shape[:2] 
    images_info.append({"file_name": v.split('\\')[-1], "id": i, "width": width, "height": height})

point = [[117,203],[48,199],[10,165],[13,122],[48,57],[113,4],[177,58],[216,121],[218,169],[179,191]]
x=[]
y=[]
for p in point:
    x.append(p[0])
    y.append(p[1])

annotations = []
suffix_zeros = math.ceil(math.log10(len(filename)))
for i,v in enumerate(filename):
    annotations.append({
                    "segmentation": [list(chain.from_iterable(zip(x, y)))],
                    "area": PolyArea(x, y),
                    "bbox": [min(x), min(y), max(x)-min(x), max(y)-min(y)],
                    "image_id": images_ids_dict[v.split('\\')[-1]],
                    "category_id": category_ids_dict[v.split('\\')[-1].split('_')[0]],
                    "id": int(len(annotations)),
                    "iscrowd": 0
                    })


coco = {
        "images": images_info,
        "categories": categories,
        "annotations": annotations
        }
print(coco)

with open('text1.json', 'w') as f:
     json.dump(coco, f)





 
# import cv2
# import numpy as np
 
# image = cv2.imread("C:/Users/User/Desktop/segmentation/sawit/train/overripe_day_141_pic_2.png")
# pos=0
# image = cv2.circle(image, (point[pos][0],point[pos][1]), 10, (255, 0, 0), -1)
# pos2=9
# image = cv2.circle(image, (point[pos2][0],point[pos2][1]), 10, (255, 0, 255), -1)

# cv2.imshow('image',image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()