from tkinter import *
from PIL import Image, ImageTk
import tkinter.font as font
import cv2
import pyautogui


w,h=pyautogui.size()
wp = int(w/5)
hp = int(h/2)


log_data = {'admin':'admin123'}


root = Tk()
root.title('FaceRecognition and Attendence')
# root.iconbitmap('ai.ico')

myFont = font.Font(size=12)


def all_children (window) :
    _list = window.winfo_children()

    for item in _list :
        if item.winfo_children() :
            _list.extend(item.winfo_children())

    return _list

def login():    
    id_val = ids.get()
    pas_val = pas.get()
    if log_data[id_val] == pas_val:
        widget_list = all_children(root)
        for item in widget_list:
            item.destroy()

        mainWindow()

#============= Image Open ====================

image = cv2.imread('./bac4.jpg')
image = cv2.blur(image,(10,10))
cv2.imwrite("bac00.jpg", image)



#Get page background and convert in ppm format
image1 = Image.open('bac00.jpg')
image1 = image1.resize((w, h), Image.ANTIALIAS)
image1.save("0.ppm", "ppm")
image1 = PhotoImage(file='0.ppm')

#Get page Recog and convert in ppm format
image2 = Image.open('face.jpg')
image2 = image2.resize((wp, hp), Image.ANTIALIAS)
image2.save("1.ppm", "ppm")
image2 = PhotoImage(file='1.ppm')

#Get page Train and convert in ppm format
image3 = Image.open('data.jpg')
image3 = image3.resize((wp, hp), Image.ANTIALIAS)
image3.save("2.ppm", "ppm")
image3 = PhotoImage(file='2.ppm')

#Get page Attendance and convert in ppm format
image4 = Image.open('att.jpg')
image4 = image4.resize((wp, hp), Image.ANTIALIAS)
image4.save("3.ppm", "ppm")
image4 = PhotoImage(file='3.ppm')


image5 = Image.open('sav.jpg')
image5 = image5.resize((int(w/34.15), int(h/12.8)), Image.ANTIALIAS)
image5.save("4.ppm", "ppm")
image5 = PhotoImage(file='4.ppm')


image6 = Image.open('back.jpg')
image6 = image6.resize((int(w/19.51), int(h/23.28)), Image.ANTIALIAS)
image6.save("5.ppm", "ppm")
image6 = PhotoImage(file='5.ppm')

shut_img = Image.open('quit.jpg')
shut_img = shut_img.resize((int(w/19.51), int(h/23.28)), Image.ANTIALIAS)
shut_img.save("quit1.ppm", "ppm")
shut_img = PhotoImage(file='quit1.ppm')


image7 = Image.open('login.jpg')
image7 = image7.resize((int(w/2),int(h/2)), Image.ANTIALIAS)
image7.save("7.ppm", "ppm")
image7 = PhotoImage(file='7.ppm')







def shutdown():
    root.destroy()


def mainWindow():


    # def shutdown():
    #     root.destroy()

    def Recog():
        panel2.destroy()
        panel3.destroy()
        panel4.destroy()


    def Train():

        def save():
            nameLabel.destroy()
            name.destroy()
            desigLabel.destroy()
            desig.destroy()
            ageLabel.destroy()
            age.destroy()
            save.destroy()
            mainWindow()




        panel2.destroy()
        panel3.destroy()
        panel4.destroy()
    
        #Creating Labels and Entry boxes
        nameLabel = Label(root, text="Enter your name please: ", bg='black', fg='white')
        nameLabel['font'] = myFont
        name = Entry(root, width=50)
        name['font'] = myFont


        desigLabel = Label(root, text="Enter your designation please: ", bg='black', fg='white')
        desigLabel['font'] = myFont
        desig = Entry(root, width=50)
        desig['font'] = myFont

        ageLabel = Label(root, text="Enter your age please: ", bg='black', fg='white')
        ageLabel['font'] = myFont
        age = Entry(root, width=50)
        age['font'] = myFont

        save = Button(root, image=image5)


        #Showing on the screen
        nameLabel.place(relx=0.01, rely=0.1, anchor=NW)
        name.place(relx=0.21, rely=0.1, anchor=NW)

        desigLabel.place(relx=0.01, rely=0.2, anchor=NW)
        desig.place(relx=0.21, rely=0.2, anchor=NW)

        ageLabel.place(relx=0.01, rely=0.3, anchor=NW)
        age.place(relx=0.21, rely=0.3, anchor=NW)

        save.place(relx=0.524, rely=0.35, anchor=NW)



    def Check():


        panel2.destroy()
        panel3.destroy()
        panel4.destroy()


    widget_list = all_children(root)
    for item in widget_list:
        item.destroy()
    
    #=================== Main Window Creation =================
    # get the image size
    w = image1.width()
    h = image1.height()

    # make the root window the size of the image
    root.geometry("%dx%d" % (w, h))

    # root has no image argument, so use a label as a panel
    #Main window back ground
    panel1 = Label(root, image=image1)
    panel1.pack(side='top', fill='both', expand='yes')

    #Route to Recog data
    panel2 = Button(root, image=image2, command = Recog,borderwidth=0, relief="flat", highlightcolor="red")
    panel2.place(relx=0.08, rely=0.2, anchor=NW)

    #Route to train data
    panel3 = Button(root, image=image3, command = Train,borderwidth=0, relief="flat")
    panel3.place(relx=0.40, rely=0.2, anchor=NW)

    #Route to check attendance
    panel4 = Button(root, image=image4, command = Check,borderwidth=0, relief="flat")
    panel4.place(relx=0.73, rely=0.2, anchor=NW)


    shut = Button(root, image=shut_img, command=shutdown)
    shut.place(relx=0.9, rely=0.05, anchor=NW)


    backbtn = Button(root, image=image6, command=mainWindow)
    backbtn.place(relx=0.83, rely=0.05, anchor=NW)

     
# get the image size
w = image1.width()
h = image1.height()

# make the root window the size of the image
root.geometry("%dx%d" % (w, h))

# root has no image argument, so use a label as a panel
#Main window back ground
panel1 = Label(root, image=image1)
panel1.pack(side='top', fill='both', expand='yes')        
panel0 = Label(root, image=image7)
panel0.place(relx=0.25, rely=0.25, anchor=NW)
shut = Button(root, image=shut_img, command=shutdown)
shut.place(relx=0.9, rely=0.05, anchor=NW)

idLabel = Label(root, text="ID:", bg='black', fg='white')
idLabel['font'] = myFont
ids = Entry(root, width=25)
ids['font'] = myFont

passLabel = Label(root, text="PASS:", bg='black', fg='white')
passLabel['font'] = myFont
pas = Entry(root, width=25)
pas['font'] = myFont

idLabel.place(relx=0.27, rely=0.27, anchor=NW)
ids.place(relx=0.32, rely=0.27, anchor=NW)

passLabel.place(relx=0.27, rely=0.32, anchor=NW)
pas.place(relx=0.32, rely=0.32, anchor=NW)

log = Button(root, text = 'login', command=login)
log.place(relx=0.462, rely=0.37, anchor=NW)





# mainWindow()





root.resizable(False, False)
root.update_idletasks()
root.maxsize(1920,1080)
root.wm_attributes('-fullscreen','true')

# start the event loop
root.mainloop()