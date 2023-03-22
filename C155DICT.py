from customtkinter import *
import customtkinter as ctk
from tkinter import *

root = ctk.CTk()
root.geometry("400x400")
lblTitle = ctk.CTkLabel(root)
lblAliasing = ctk.CTkLabel(root)
lblTkinter = ctk.CTkLabel(root)
lblMatplotlib = ctk.CTkLabel(root)
lblAliasing.configure(text="")
lblTkinter.configure(text="")
lblMatplotlib.configure(text="")
lblTitle.configure(text="Coding Vocabulary")
lblTitle.place(relx=0.5,rely=0.1,anchor=CENTER)

codeVocab = {"Aliasing":"Aliasing is giving nicknames to store references to some values.", "Tkinter":"It is a GUI Library in python.", "Matplotlib":"This is a plotting and data visualization library in python."}

def Aliasing():
    lblAliasing.configure(text=str(codeVocab["Aliasing"]))
def Tkinter():
    lblTkinter.configure(text=str(codeVocab["Tkinter"]))
def Matplotlib():
    lblMatplotlib.configure(text=str(codeVocab["Matplotlib"]))
    
btnAlia = ctk.CTkButton(root, text="Click Here To Learn The Meaning Of Aliasing", command=Aliasing)
btnTtk = ctk.CTkButton(root, text="Click Here To Learn The Meaning Of Tkinter", command=Tkinter)
btnMpl = ctk.CTkButton(root, text="Click Here To Learn The Meaning Of Matplotlib", command=Matplotlib)

lblAliasing.place(relx=0.5,rely=0.25,anchor=CENTER)
btnAlia.place(relx=0.5,rely=0.35,anchor=CENTER)
lblTkinter.place(relx=0.5,rely=0.5,anchor=CENTER)
btnTtk.place(relx=0.5,rely=0.6,anchor=CENTER)
lblMatplotlib.place(relx=0.5,rely=0.8,anchor=CENTER)
btnMpl.place(relx=0.5,rely=0.9,anchor=CENTER)

root.mainloop()