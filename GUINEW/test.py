from tkinter import *
from PIL import Image, ImageTk, ImageSequence
from test1 import Log
import pyautogui

w,h=pyautogui.size()
class App:
    def __init__(self, parent):
        self.parent = parent
        self.canvas = Canvas(parent, width=w, height=h,highlightthickness = 0, bd = 0)
        self.canvas.pack()
        self.sequence = [ImageTk.PhotoImage(img)
                            for img in ImageSequence.Iterator(
                                    Image.open(
                                    r'./createImage/2.gif'))]
        self.image = self.canvas.create_image(960,540, image=self.sequence[0])
        self.animate(1)
    def animate(self, counter):
        self.canvas.itemconfig(self.image, image=self.sequence[counter])
        self.parent.after(100, lambda: self.animate((counter+1) % len(self.sequence)))






def shutdown(event):
    root.destroy()








root = Tk()
root.resizable(False, False)
root.geometry("%dx%d" % (w, h))
root.update_idletasks()
root.maxsize(1920,1080)
root.wm_attributes('-fullscreen','true')













# root.bind("<Shift-BackSpace>",back)
root.bind("<Escape>", shutdown)

app = App(root)
log = Log(root)
root.mainloop()