import cv2
import os
import numpy as np
import csv



#for face detection
def faceDetection(test_img):
    gray_img = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)
    face_haar_cascade = cv2.CascadeClassifier('./HaarCascade/haarcascade_frontalface_default.xml')
    faces= face_haar_cascade.detectMultiScale(gray_img, scaleFactor= 1.32, minNeighbors= 5)

    return faces, gray_img

#for labeling each file the folder name
def labels_for_training_data(directory):
    faces = []
    faceID = []

    for path, subdirnames, filenames in os.walk(directory):
        for filename in filenames:
            if filename.startswith("."):
                print("Skipping system file")
                continue

            id = os.path.basename(path)
            img_path = os.path.join(path, filename)
            print("img_path: ", img_path)
            print("id: ", id)
            test_img = cv2.imread(img_path)
            if test_img is None:
                print("Image not loaded properly")
                continue
            faces_rect, gray_img = faceDetection(test_img)
            if len(faces_rect) != 1:
                continue #since we are assuming only single person images are being fed to classifier
            (x,y,w,h)= faces_rect[0]
            roi_gray= gray_img[y:y+h, x:x+w]
            faces.append(roi_gray)
            faceID.append(int(id))

    return faces, faceID


#to train the classifier to detect the image
def train_classifier(faces, faceID):
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    face_recognizer.train(faces, np.array(faceID))
    return face_recognizer

#drawing rectangles on the faces
def draw_rect(test_img, face):
    (x,y,w,h) = face
    cv2.rectangle(test_img, (x, y), (x+w, y+h), (255, 0, 0), thickness=1)

#putting text on the faces
def put_text(test_img, text, x, y, font, size, color, thickness):
    cv2.putText(test_img, text, (x, y), font, size, color, thickness)



#making folder for new person entry
def make_dir():
    name = 0
    for path, subdirnames, filenames in os.walk('./test'):
        
        if subdirnames:
            for subdirname in subdirnames:
                for i in range (0, 100): #the range means how many persons you can enter
                    if subdirname == str(i):
                        print("Skipping system folder")
                        break
                        
                name += 1
                    

    path = './test/'  
    os.makedirs(path + str(name))
    return str(name)

#deleting the folder made if the person's data not entered correctly
def del_dir(name):
    path = './test/'  
    os.removedirs(path+ str(name))


#saving the names of new entered persons
def write_person_data(file,id,name):
    with open(file+'.csv', 'a') as fa:
        csv_writer =  csv.writer(fa)
        csv_writer.writerow([id,name])

#saving the details of new entered persons
def write_person_details(file,id,name,desig,age):
    with open(file+'.csv', 'a') as fa:
        csv_writer =  csv.writer(fa)
        csv_writer.writerow([id,name,desig,age])




#reading persons names from csv file
def read_person_data(fil):
    result = []
    with open(fil+'.csv', 'r') as fr:
        csv_reader = csv.reader(fr)
        if csv_reader:
            for i in csv_reader:
                if len(i) >1:
                    id = i.pop(0)
                    dic = {}
                    dic[id]=i
                    result.append(dic)
    return result

def train_data():
    faces, faceID = labels_for_training_data('./test')
    face_recognizer = train_classifier(faces, faceID)
    face_recognizer.save('trainingData.yml')