from tkinter import *
from recog import Recog
from train import Train
from check import Check
from functions import all_children


def Home(root, img_bg, img_recog, img_train, img_check,img_tr_save):

    widget_list = all_children(root)
    for item in widget_list:
        item.destroy()
    # root has no image argument, so use a label as a panel
    #Main window back ground
    bg_panel = Label(root, image=img_bg)
    bg_panel.pack(side='top', fill='both', expand='yes')  

    #Route to Recog data
    rg_panel = Button(root, image=img_recog, command = lambda: Recog(root,img_bg),borderwidth=0, relief="flat", highlightcolor="red")
    rg_panel.place(relx=0.08, rely=0.2, anchor=NW)

    #Route to train data
    tr_panel = Button(root, image=img_train, command = lambda: Train(root,img_bg,img_tr_save),borderwidth=0, relief="flat")
    tr_panel.place(relx=0.40, rely=0.2, anchor=NW)

    #Route to check attendance
    ch_panel = Button(root, image=img_check, command = lambda: Check(root,img_bg),borderwidth=0, relief="flat")
    ch_panel.place(relx=0.73, rely=0.2, anchor=NW)
