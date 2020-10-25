import cv2
import PIL 
from PIL import Image
from PIL import ImageTk
from tkinter import *
import numpy as np






class videoStream:
    panel = None
    ventana = None
    camera = None

    def __init__(self):
        self.ventana = Tk()
        self.ventana.title('Stream')
        self.ventana.geometry("400x400")

        self.panel = Label(self.ventana)
        self.panel.pack()

        self.camera = cv2.VideoCapture(0)
        self.camera1()
        self.ventana.mainloop()

    def camera1(self):
        _,frame = self.camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = np.asarray(frame)
        frame = PIL.Image.fromarray(frame)
        frame = ImageTk.PhotoImage(frame)
        self.panel.configure(image=frame)
        self.panel.image = frame
        self.panel.after(1,self.camera)



