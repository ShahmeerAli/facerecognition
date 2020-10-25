from tkinter import *

root = Tk()


canvas = Canvas(root, width = 600, height = 600)      
canvas.pack()      
img = PhotoImage(file="bac.ppm")      
canvas.create_image(100,100, image=img)   

def save_data():

    def continue_data():
        newWindow.destroy()
        save["state"] ="active"
        name.delete(0, END)
        desig.delete(0, END)
        age.delete(0, END)

    newWindow = Toplevel(root)
    text = 'Hello '+name.get()+ ', you are '+age.get()+' years old and working as '+desig.get()    
    resultLabel = Label(newWindow, text=text).grid(row=0,column=0)
    continue_ = Button(newWindow, text="continue", padx=10, pady=5, command=continue_data).grid(row=1,column=0)

    if 'normal' == newWindow.state():
        save["state"] ="disabled"


 
#Creating Labels and Entry boxes
nameLabel = Label(root, text="Enter your name please: ", bg='black', fg='white')
name = Entry(root, width=50)

desigLabel = Label(root, text="Enter your designation please: ")
desig = Entry(root, width=50)

ageLabel = Label(root, text="Enter your age please: ")
age = Entry(root, width=50)


save = Button(root, text="Save", padx=10, pady=5, command=save_data)


#Showing on the screen
nameLabel.place(relx=0.01, rely=0.1, anchor=NW)
name.place(relx=0.25, rely=0.1, anchor=NW)

# desigLabel.place(relx=0.99, rely=1.0, anchor=SE)
# desig.place(relx=0.99, rely=1.0, anchor=SE)

# ageLabel.place(relx=0.99, rely=1.0, anchor=SE)
# age.place(relx=0.99, rely=1.0, anchor=SE)

# save.place(relx=0.99, rely=1.0, anchor=SE)



root.mainloop()