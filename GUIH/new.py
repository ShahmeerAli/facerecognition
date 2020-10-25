from tkinter import *
from PIL import Image
import tkinter.font as font



root = Tk()
root.title('FaceRecognition and Attendence')
# root.iconbitmap('ai.ico')

myFont = font.Font(size=12)

#============= Image Open ====================

#Get page background and convert in ppm format
image1 = Image.open('bac.jpg')
image1.save("0.ppm", "ppm")
image1 = PhotoImage(file='0.ppm')

#Get page Recog and convert in ppm format
image2 = Image.open('face.jpg')
image2 = image2.resize((350, 450), Image.ANTIALIAS)
image2.save("1.ppm", "ppm")
image2 = PhotoImage(file='1.ppm')

#Get page Train and convert in ppm format
image3 = Image.open('data.jpg')
image3 = image3.resize((350, 450), Image.ANTIALIAS)
image3.save("2.ppm", "ppm")
image3 = PhotoImage(file='2.ppm')

#Get page Attendance and convert in ppm format
image4 = Image.open('att.jpg')
image4 = image4.resize((350, 450), Image.ANTIALIAS)
image4.save("3.ppm", "ppm")
image4 = PhotoImage(file='3.ppm')


image5 = Image.open('save.jpg')
image5 = image5.resize((70, 70), Image.ANTIALIAS)
image5.save("4.ppm", "ppm")
image5 = PhotoImage(file='4.ppm')


image6 = Image.open('back.jpg')
image6 = image6.resize((70, 70), Image.ANTIALIAS)
image6.save("5.ppm", "ppm")
image6 = PhotoImage(file='5.ppm')






    



def mainWindow():
    
    def Recog():
        panel2.destroy()
        panel3.destroy()
        panel4.destroy()

        back = Button(root, text="Back", padx=10, pady=5, command=mainWindow)
        back.place(relx=0.5, rely=0.5, anchor=NW)
        


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

        back = Button(root, image=image6, command=save)
        save = Button(root, image=image5)


        #Showing on the screen
        nameLabel.place(relx=0.01, rely=0.1, anchor=NW)
        name.place(relx=0.23, rely=0.1, anchor=NW)

        desigLabel.place(relx=0.01, rely=0.2, anchor=NW)
        desig.place(relx=0.23, rely=0.2, anchor=NW)

        ageLabel.place(relx=0.01, rely=0.3, anchor=NW)
        age.place(relx=0.23, rely=0.3, anchor=NW)

        save.place(relx=0.5, rely=0.4, anchor=NW)
        back.place(relx=0.55, rely=0.4, anchor=NW)


    def Check():



        panel2.destroy()
        panel3.destroy()
        panel4.destroy()
    
        back = Button(root, text="Back", padx=10, pady=5, command=mainWindow)
        back.place(relx=0.5, rely=0.5, anchor=NW)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
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
    panel2 = Button(root, image=image2, command = Recog)
    panel2.place(relx=0.07, rely=0.1, anchor=NW)

    #Route to train data
    panel3 = Button(root, image=image3, command = Train)
    panel3.place(relx=0.38, rely=0.1, anchor=NW)

    #Route to check attendance
    panel4 = Button(root, image=image4, command = Check)
    panel4.place(relx=0.69, rely=0.1, anchor=NW)




mainWindow()



# start the event loop
root.mainloop()