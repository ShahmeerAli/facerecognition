from tkinter import *

root = Tk()


def continue_data(window):
        window.destroy()
        save["state"] ="active"

def save_data():


    newWindow = Toplevel(root)
    text = 'Hello '+name.get()+ ', you are '+age.get()+' years old and working as '+desig.get()    
    resultLabel = Label(newWindow, text=text).grid(row=0,column=0)
    save = Button(newWindow, text="continue", padx=10, pady=5, command=continue_data(newWindow)).grid(row=1,column=0)

    if 'normal' == newWindow.state():
        save["state"] ="disabled"


 
#Creating Labels and Entry boxes
nameLabel = Label(root, text="Enter your name please: ")
name = Entry(root, width=50)

desigLabel = Label(root, text="Enter your designation please: ")
desig = Entry(root, width=50)

ageLabel = Label(root, text="Enter your age please: ")
age = Entry(root, width=50)


save = Button(root, text="Save", padx=10, pady=5, command=save_data)


#Showing on the screen
nameLabel.grid(row=0,column=0)
name.grid(row=0,column=1)

desigLabel.grid(row=1,column=0)
desig.grid(row=1,column=1)

ageLabel.grid(row=2,column=0)
age.grid(row=2,column=1)

save.place(relx=0.99, rely=1.0, anchor=SE)


root.minsize(width=600,height=101)
root.mainloop()