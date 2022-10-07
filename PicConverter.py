import os 
import cv2

os.chdir("C:/Users/User/Desktop/Mask_sawit")
path="C:/Users/User/Desktop/Mask_sawit1"
i=1
for file in os.listdir():
    ori=cv2.imread(file)
    ori = cv2.resize(ori, (1200,800))
    cv2.imwrite(path+"/F_"+str(i)+".png", ori)
    i+=1
print("Done")
    
