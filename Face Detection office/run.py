import cv2
import os
import numpy as np
import functions as fr 



#This file is to recognize faces which are trained




# test_img = cv2.imread('./testImages/tw1.jpg')

face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('./trainingData.yml')






cap = cv2.VideoCapture(0)


att = []
for i in range(100):
    
    ret, test_img = cap.read()
    face_detected, gray_img = fr.faceDetection(test_img)


    #detecting and resizing image
    for (x,y,w,h) in face_detected:
        cv2.rectangle(test_img, (x,y), (x+w, y+h), (255,0,0), thickness=7)

        resized_img = cv2.resize(test_img, (1000, 700))
        cv2.imshow("face detection", resized_img)
        cv2.waitKey(10)

    #predicting with names and draw rectangles
    for face in face_detected:
        (x,y,w,h) = face
        roi_gray = gray_img[y:y+h, x:x+w]
        label, confidence = face_recognizer.predict(roi_gray)
        print("confidence: ", confidence)
        print("label: ", label)
        fr.draw_rect(test_img, face)

        data = fr.read_person_data('data')
        predicted_name = data[label][str(label)][0]
        if confidence < 45:
            fr.put_text(test_img, predicted_name, x, y-10, cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 0), 1)
            att.append(label)
    
    
    #resizing images
    resized_img = cv2.resize(test_img, (1000, 700))
    cv2.imshow("face detection", resized_img)
    
    #default break
    if cv2.waitKey(10) == ord('q'):
        break

total = 0
index = 0
for i in range(len(att)):
    count = 0
    for j in range(len(att)):
        if att[i] == att[j]:
            count+=1 
    if count > total:
        total = count
        index = j

print(str(total) +' times matched')
if total > 60:
    data = fr.read_person_data('data')
    predicted_name = data[index][str(index)][0]
    print(predicted_name+ " is present")
cap.release()
cv2.destroyAllWindows
