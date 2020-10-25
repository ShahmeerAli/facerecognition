from functions import all_children 
from tkinter import *



def Recog(root,img_bg):
    widget_list = all_children(root)
    for item in widget_list:
        item.destroy()

    bg_panel = Label(root, image=img_bg)
    bg_panel.pack(side='top', fill='both', expand='yes')

    