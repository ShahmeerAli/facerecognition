from tkinter import *
import tkinter.font as font
import pyautogui
from functions import all_children
from home import Home



def callBack(root,img_bg,img_recog,img_train,img_check,img_tr_save):
    Home(root,img_bg,img_recog,img_train,img_check,img_tr_save)


def Login(root,img_bg, img_log, img_recog, img_train, img_check,img_tr_save):

    log_data = {'admin':'admin123'}

    def fn_none():
        return


    def authorized(event):    
        id_val = ids.get()
        pas_val = pas.get()
        if log_data[id_val] == pas_val:
            widget_list = all_children(root)
            for item in widget_list:
                item.destroy()
            Home(root,img_bg,img_recog,img_train,img_check,img_tr_save)
        return


    w,h=pyautogui.size()
    f_size = int(w/165)
    myFont = font.Font(size=f_size)

    bg_panel = Label(root, image=img_bg)
    bg_panel.pack(side='top', fill='both', expand='yes')   

    login_panel = Label(root, image=img_log)
    login_panel.place(relx=0.25, rely=0.25, anchor=NW)

    lw = int(w/40)
    idLabel = Label(root, text="ID:", bg='black', fg='white')
    idLabel['font'] = myFont
    ids = Entry(root, width=lw)
    ids['font'] = myFont

    passLabel = Label(root, text="PASS:", bg='black', fg='white')
    passLabel['font'] = myFont
    pas = Entry(root,show="*", width=lw)
    pas['font'] = myFont

    idLabel.place(relx=0.27, rely=0.27, anchor=NW)
    ids.place(relx=0.3, rely=0.27, anchor=NW)

    passLabel.place(relx=0.27, rely=0.32, anchor=NW)
    pas.place(relx=0.3, rely=0.32, anchor=NW)

    log = Button(root, text = 'login',width=int(lw/2.5))
    log.bind('<Return>', authorized)
    log.bind('<Button-1>', authorized)
    log.place(relx=0.382, rely=0.37, anchor=NW)