from tkinter import *
import tkinter.font as font
from PIL import Image, ImageTk, ImageSequence
import pyautogui
from functions import all_children
from home import Home
# from test import App




# def callBack(root,img_bg,img_recog,img_train,img_check,img_tr_save):
#     Home(root,img_bg,img_recog,img_train,img_check,img_tr_save)



class Log:
    def __init__(self,parent):
        self.img_log = PhotoImage(file='./createImage/log.png')
        image = Image.open('./createImage/lgbtn1.jpg')
        image = image.resize((int(120),int(50)), Image.ANTIALIAS)
        image.save("./createImage/logbtn.ppm", "ppm")
        self.img_logbtn = PhotoImage(file='./createImage/logbtn.ppm')
        self.parent = parent
        self.Login(self.parent,self.img_log,self.img_logbtn)



    def Login(self,parent,img_log,img_logbtn):

        log_data = {'admin':'admin123'}

        def fn_none():
            return


        def authorized(event):    
            id_val = ids.get()
            pas_val = pas.get()
            if log_data[id_val] == pas_val:
                log.destroy()
                # app = App(parent)
                # Home(parent,img_bg,img_recog,img_train,img_check,img_tr_save)
            return


        w,h=pyautogui.size()
        f_size = int(w/165)
        myFont = font.Font(size=f_size)

        login_panel = Label(self.parent, image=self.img_log,highlightthickness = 0, bd = 0)
        login_panel.place(relx=0.1, rely=0.1, anchor=NW)
        large_font = ('Verdana',15)
        lw = int(w/30)
        idLabel = Label(self.parent, text="USER ID:", bg='black', fg='white')
        idLabel['font'] = large_font
        ids = Entry(self.parent, width=lw)
        ids['font'] = large_font

        passLabel = Label(self.parent, text="PASSWORD:", bg='black', fg='white')
        passLabel['font'] = large_font
        pas = Entry(self.parent,show="*", width=lw)
        pas['font'] = large_font

        idLabel.place(relx=0.23, rely=0.36, anchor=NW)
        ids.place(relx=0.33, rely=0.36, anchor=NW)

        passLabel.place(relx=0.23, rely=0.45, anchor=NW)
        pas.place(relx=0.33, rely=0.45, anchor=NW)


       
        log = Button(parent, image=self.img_logbtn,highlightthickness = 0, bd = 0)
        log.bind('<Return>', authorized)
        log.bind('<Button-1>', authorized)
        log.place(relx=0.67, rely=0.55, anchor=NW)