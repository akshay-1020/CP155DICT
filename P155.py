from tkinter import *
import random
root = Tk()
root.geometry("400x400")
c = {0:"snow",1:"gold",2:"NavajoWhite3",3:"dark olive green",4:"SkyBlue1",5:"cornsilk2",6:"cornflower blue",7:"salmon",8:"MistyRose2",9:"olive drab"}
def changeColor():
    root.configure(bg=str(c[random.randint(0,len(c)-1)]))
btnchangeColor = Button(root, text="Change Color", command=changeColor).place(relx=0.5,rely=0.5,anchor=CENTER)
root.mainloop()