from tkinter import *
# from PIL import Image, ImageTk
from pics import create_pics
import pyautogui
from login import Login,callBack
from home import Home


#to run a python script with code
# import importlib
# importlib.import_module('new')

w,h=pyautogui.size()

root = Tk()
root.title('FaceRecognition and Attendence')
# root.iconbitmap('ai.ico')


# make the root window the size of the image
root.geometry("%dx%d" % (w, h))




#====================== Images ============================
create_pics()
img_bg = PhotoImage(file='./createImage/0.ppm')
img_log = PhotoImage(file='./createImage/1.ppm')
img_recog = PhotoImage(file='./createImage/2.ppm')
img_train = PhotoImage(file='./createImage/3.ppm')
img_check = PhotoImage(file='./createImage/4.ppm')
img_tr_save = PhotoImage(file='./createImage/5.ppm')


def shutdown(event):
    root.destroy()

def back(event):
    callBack(root,img_bg,img_recog,img_train,img_check,img_tr_save)

Login(root,img_bg,img_log,img_recog,img_train,img_check,img_tr_save)


root.resizable(False, False)
root.update_idletasks()
root.maxsize(1920,1080)
root.wm_attributes('-fullscreen','true')


root.bind("<Shift-BackSpace>",back)
root.bind("<Escape>", shutdown)
# start the event loop
root.mainloop()