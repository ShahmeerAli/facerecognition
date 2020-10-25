from functions import all_children 
from tkinter import *
import tkinter.font as font
import pyautogui

def Train(root,img_bg,img_tr_save ):


    w,h=pyautogui.size()
    f_size = int(w/165)
    myFont = font.Font(size=f_size)
    widget_list = all_children(root)
    for item in widget_list:
        item.destroy()

    bg_panel = Label(root, image=img_bg)
    bg_panel.pack(side='top', fill='both', expand='yes')        

    def save():
        nameLabel.destroy()
        name.destroy()
        desigLabel.destroy()
        desig.destroy()
        ageLabel.destroy()
        age.destroy()
        save.destroy()
    
    lw = int(w/39.6)
    #Creating Labels and Entry boxes
    nameLabel = Label(root, text="NAME: ", bg='black', fg='white')
    nameLabel['font'] = myFont
    name = Entry(root, width=lw)
    name['font'] = myFont


    desigLabel = Label(root, text="DESIGNATION: ", bg='black', fg='white')
    desigLabel['font'] = myFont
    desig = Entry(root, width=lw)
    desig['font'] = myFont

    ageLabel = Label(root, text="AGE: ", bg='black', fg='white')
    ageLabel['font'] = myFont
    age = Entry(root, width=lw)
    age['font'] = myFont

    idcardLabel = Label(root, text="IDENTITY CARD: ", bg='black', fg='white')
    idcardLabel['font'] = myFont
    idcard = Entry(root, width=lw)
    idcard['font'] = myFont


    #Route to scan face
    scan_panel = Button(root, image=img_tr_save, command = None,borderwidth=0, relief="flat")
    scan_panel.place(relx=0.1, rely=0.4, anchor=NW)


    #Showing on the screen
    nameLabel.place(relx=0.01, rely=0.1, anchor=NW)
    name.place(relx=0.06, rely=0.1, anchor=NW)

    desigLabel.place(relx=0.01, rely=0.15, anchor=NW)
    desig.place(relx=0.09, rely=0.15, anchor=NW)

    ageLabel.place(relx=0.01, rely=0.2, anchor=NW)
    age.place(relx=0.06, rely=0.2, anchor=NW)

    idcardLabel.place(relx=0.01, rely=0.25, anchor=NW)
    idcard.place(relx=0.09, rely=0.25, anchor=NW)