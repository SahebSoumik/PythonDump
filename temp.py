from tkinter import *
from tkinter import messagebox
import random

def submit():
     num1=int(e1.get())

     tem=(num1*1.8)+32

     messagebox.showinfo('Value','The temp is : {}'.format(tem))


root=Tk()

root.geometry('500x500')

Label(root,text='Enter the Temp in celcious : ').grid(row=0,column=0)
e1=Entry(root)
e1.grid(row=0,column=1)

Button(root,text='Convert',command=submit).grid(row=3,column=3)
