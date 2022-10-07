import cv2
import math

img = cv2.imread("C:/Users/User/Downloads/image.png") 

img_shape = img.shape
tile_size = (1440, 1440)
offset = (1440, 1440)
print(img_shape)

for i in range(int(math.ceil(img_shape[0]/(offset[1] * 1.0)))):
    for j in range(int(math.ceil(img_shape[1]/(offset[0] * 1.0)))):
        y1 = offset[1]*i
        y2 = min(offset[1]*i+tile_size[1], img_shape[0])
        x1 = offset[0]*j
        x2 = min(offset[0]*j+tile_size[0], img_shape[1])
        cropped_img = img[y1:y2, x1:x2]
        # Debugging the tiles
        cv2.imwrite("C:/Users/User/Desktop/test1overlay/tiling_r" + str(i) + "_c" + str(j) + ".png", cropped_img)
        # print(xmin,ymin, xmax,ymax)
        
        
        
# img = cv2.imread("C:/Users/User/Downloads/JPEG Format-20211126T045337Z-001/JPEG Format/Block20141831ha_Orthomosaic_export_WedNov10093523386951.jpg") 
# imW = math.ceil(img.shape[1]/4)
# imH = math.ceil(img.shape[0]/4)

# print(imW,imH)
 
# img=cv2.resize(img,(imW,imH))
# cv2.imwrite("C:/Users/User/Desktop/newIMG.png", img)