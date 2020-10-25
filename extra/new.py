import cv2
import os
import numpy as np
import functions as fr 
import test



file_name = '0'

cap = cv2.VideoCapture(0)
# file_name = test.make_dir()

while True:
    file_name = test.make_dir()
    ret, test_img = cap.read()
    face_detected, gray_img = fr.faceDetection(test_img)

    if len(face_detected) < 2:
        text = 'detected'
    else:
        text = 'more than one face detected'
        test.del_dir(file_name)
        break

    for face in face_detected:
        (x,y,w,h) = face
        fr.draw_rect(test_img, face)
        fr.put_text(test_img, text, x, y)


    resized_img = cv2.resize(test_img, (1000, 700))
    cv2.imshow("face detection", resized_img)
    if cv2.waitKey(10) == ord('q'):
        break


cap.release()
cv2.destroyAllWindows