import pyautogui
import cv2
from PIL import Image as img
from PIL import ImageTk
from tkinter import *




w,h=pyautogui.size()
wp = int(w/5)
hp = int(h/2)

def create_pics():
    #============= Root ====================
    #Bluring background Image
    image = cv2.imread('./images/back.jpg')
    image = cv2.blur(image,(10,10))
    cv2.imwrite("./images/back_blur.jpg", image)

    #Background Image
    image = img.open('./images/back_blur.jpg')
    image = image.resize((w, h), img.ANTIALIAS)
    image.save("./createImage/0.ppm", "ppm")




    #================= Login Panel ==================================
    #Image for login Panel
    image = img.open('./images/login.jpg')
    image = image.resize((int(w/2),int(h/2)), img.ANTIALIAS)
    image.save("./createImage/1.ppm", "ppm")




    #=============== Home Page =======================================
    #Image for recog Button
    image = img.open('./images/recog.jpg')
    image = image.resize((wp, hp), img.ANTIALIAS)
    image.save("./createImage/2.ppm", "ppm")


    #Image for train Button
    image = img.open('./images/train.jpg')
    image = image.resize((wp, hp), img.ANTIALIAS)
    image.save("./createImage/3.ppm", "ppm")


    #Image for check Button
    image = img.open('./images/check.jpg')
    image = image.resize((wp, hp), img.ANTIALIAS)
    image.save("./createImage/4.ppm", "ppm")






    # #================== Recog Page =====================================











    ws = int(w/6.6)
    hs = int(h/5.4)
    # #=================== Train Page =======================================
    #Image for save data
    image = img.open('./images/save_tr.jpg')
    image = image.resize((ws, hs), img.ANTIALIAS)
    image.save("./createImage/5.ppm", "ppm")





    #==================== Check Page =======================================






