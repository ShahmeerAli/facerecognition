import cv2
import os
import numpy as np
import functions as fr 
import matplotlib.pyplot as plt
import test 


name = str(test.make_dir())

cap = cv2.VideoCapture(0)


while True:
    ret, test_img = cap.read()
    face_detected, gray_img = fr.faceDetection(test_img)

    for (x,y,w,h) in face_detected:
        cv2.rectangle(test_img, (x,y), (x+w, y+h), (255,0,0), thickness=7)

        resized_img = cv2.resize(test_img, (1000, 700))
        cv2.imshow("face detection", resized_img)
        cv2.waitKey(10)


    for face in face_detected:
        (x,y,w,h) = face
        fr.draw_rect(test_img, face)
   
   


        # img = cv2.cvtColor(test_img, cv2.COLOR_BGR2RGB)
        # plt.imshow(gray_img)
        # plt.xticks([])
        # plt.yticks([])
        # img_name = str(i)
        # path = '/home/shahmir/Desktop/Face Detection/test/'  
        # plt.savefig(path+ name+ '/'+ img_name)
        
    
        


    resized_img = cv2.resize(test_img, (1000, 700))
    cv2.imshow("face detection", resized_img)
    if cv2.waitKey(10) == ord('q'):
        break


cap.release()
cv2.destroyAllWindows