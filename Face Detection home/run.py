import cv2
import os
import numpy as np
import functions as fr 

# test_img = cv2.imread('./testImages/tw1.jpg')

face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('./trainingData.yml')






cap = cv2.VideoCapture(0)

while cap.isOpened():
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

        data = fr.read_person_data()
        predicted_name = data[label]
        if confidence < 60:
            fr.put_text(test_img, predicted_name, x, y-10, cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 0), 1)
    
    
    
    #resizing images
    resized_img = cv2.resize(test_img, (1000, 700))
    cv2.imshow("face detection", resized_img)
    
    #default break
    if cv2.waitKey(10) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows
