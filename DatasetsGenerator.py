'''
import cv2
vid=cv2.VideoCapture("C:/Users/User/Downloads/DJI_0245.MP4")
frame_width=int(vid.get(3))
frame_height=int(vid.get(4))

print("WIDTH is ", frame_width)
print("HEIGHT is ", frame_height)

i=0

while(vid.isOpened()):
    ret,frame=vid.read()
    
    if ret==True:
        cv2.imwrite("C:/Users/User/Documents/EBTECH/dataset/cannon/C_"+str(i)+".jpg", frame)
        i=i+1
        #cv2.imshow("frame",frame)
        print("Generating")
        
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
        
    elif ret==False:
        print("Done Generate")
        break
    
vid.release()
cv2.destroyAllWindows()

'''
import cv2
vid=cv2.VideoCapture("C:/Users/User/Downloads/DJI_0245.MP4")
frame_width=int(vid.get(3))
frame_height=int(vid.get(4))

print("WIDTH is ", frame_width)
print("HEIGHT is ", frame_height)

i=0
no=1400
while(vid.isOpened()):
    ret,frame=vid.read()
    
    if ret==True:
        if i == no:
            cv2.imwrite("C:/Users/User/Documents/EBTECH/dataset/cannon/C_"+str(i)+".jpg", frame)
            no=no+100
            print("Generating")
        i=i+1
        #cv2.imshow("frame",frame)
        print("Do Nothing")
        
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
        
    elif ret==False:
        print("Done Generate")
        break
    
vid.release()
cv2.destroyAllWindows()
