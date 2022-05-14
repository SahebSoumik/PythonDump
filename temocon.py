from tkinter import *
from tkinter import messagebox

root=Tk()

def save():
     num1=int(e1.get())

     fer=(num1*(9/5))+32

     messagebox.showinfo('Value','The ferhenite is  : {}'.format(fer))

Label(root,text='Enter your temp in celcious : ').grid(row=0,column=0)
e1=Entry(root)
e1.grid(row=1,column=0)

Button(root,text='Submit',command=save).grid(row=3,column=3)
