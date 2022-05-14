from tkinter import *

root=Tk()

def click():
     entry1=e1.get()
     entry2=e2.get()

     print("Successfully logged in",entry1)

Label(root,text="Enter your name : ").grid(row=0,column=1)
e1=Entry(root)
e1.grid(row=0,column=2)

Label(root,text="Enter your password : ").grid(row=1,column=1)
e2=Entry(root)
e2.grid(row=1,column=2)

Button(root,text="Submit",command=click).grid(row=3,column=3)
