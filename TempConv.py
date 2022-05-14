from tkinter import *
from tkinter import messagebox

root=Tk()


def temp():
     num=int(e1.get())

     far=((num*1.8)+32)

     messagebox.showinfo("Demo","The farhenite : {}".format(far))

Label(root,text="Enter the temp in celcious : ").grid(row=0,column=0)
e1=Entry(root)
e1.grid(row=0,column=1)

Button(root,text="Submit",command=temp).grid(row=1,column=1)
