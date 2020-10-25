from tkinter import *

class MainFrame(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.createWidget()

    def createWidget(self):
        self.innerFrame = Frame(self)
        # self.innerFrame.master.resizable(width=False, height=False)  # ====> this place raise error:'MainFrame' object has no attribute 'resizable'
        # self.innerFrame.master.maxsize(width=300, height=400)
        for l in range():
            label = Label(self.innerFrame, text="label" + str(l))
            label.pack()
        self.innerFrame.pack()

if __name__ == '__main__':
    top = Tk()
    # top.resizable(width=False, height=False)
    top.minsize(width=400, height=600)
    app = MainFrame(top)
    app.pack()
    app.mainloop()