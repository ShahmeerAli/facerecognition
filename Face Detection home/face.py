import cv2
import os
import numpy as np


import functions as fr 


cap = cv2.VideoCapture(0) #capture video from webcam

#reading data from csv file
data = fr.read_person_data()
id = len(data)



dele = 0
dir_name = ''
while True:
    pr_name = input("Enter Your Name : \n") #dict of the persons entered in the database
    fr.write_person_data(id, pr_name)
    capture = input("press s to capture \n") #to record new person's data
    if capture == 's':
        name = fr.make_dir() #creating a new folder for each person
        dir_name = name # for making global



    #======================== for taking samples ==========================
    br = 1 #for breaking loop
    while capture == 's':
        ret, test_img = cap.read()
        face_detected, gray_img = fr.faceDetection(test_img)


        #checking for only single face and saving image from webcam
        if len(face_detected) < 2:
            text = 'Detected' + str(br) + ' of 20'
            # img = cv2.cvtColor(test_img, cv2.COLOR_BGR2RGB)
            image = str(br)
            path = '/home/shahmir/Desktop/Face Detection/test/'  
            img_nm = path+ name+ '/'+ image + '.jpg'
            cv2.imwrite(img_nm, test_img)
            br += 1
        # if two faces break loop and try again
        else:
            text = 'more than one face detected try again'
            fr.del_dir(name)
            break
        

        #draw rectangle on face
        for face in face_detected:
            (x,y,w,h) = face
            fr.draw_rect(test_img, face)
            fr.put_text(test_img, text, x, y-10, cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 0), 1)


        #Resize if or if not image is too large
        resized_img = cv2.resize(test_img, (1000, 700))
        cv2.imshow("face detection", resized_img)


        dele = br #for making global

        #break after snapping 20 pics    
        if br == 21:
            break

        
        #default break
        if cv2.waitKey(10) == ord('q'):
            break
        
    id += 1
    capture = 'a'


    #======================= for samples taken  ============================
    while capture == 'a':
        ret, test_img = cap.read()
        face_detected, gray_img = fr.faceDetection(test_img)

        #draw rectangle on face
        for face in face_detected:
            (x,y,w,h) = face
            fr.draw_rect(test_img, face)
            text = 'Samples Taken'
            fr.put_text(test_img, text, x, y-10, cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 0), 2)


        #Resize if or if not image is too large
        resized_img = cv2.resize(test_img, (1000, 700))
        cv2.imshow("face detection", resized_img)
        

        for i in range(100):
            if i == 99:
                capture ='s'

        #default break
        if cv2.waitKey(10) == ord('q'):
            break
    
    #training the data for recognization
    fr.train_data()



#if anyhow 20 pics are not saved delete the folder and do it again
if dele!= 21:
    fr.del_dir(name)
    print("20 pics not entered successfully")



cap.release()
cv2.destroyAllWindows