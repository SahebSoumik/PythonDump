#currency converter
from tkinter import *
from tkinter  import messagebox

def submit():
     num1=int(e1.get())
     num2=int(e2.get())

     if num2==1:
          messagebox.showinfo('Value','The amount is : {}'.format(num1/75))
     elif num2==2:
          messagebox.showinfo('Value','The Amount is : {}'.format(num1/90))
     elif num2==3:
          messagebox.showinfo('Value','The amount is : {}'.format(num1/20))
     else:
          messagebox.showinfo('Value','The choice is invalid')
root=Tk()

Label(root,text="Enter the amount in INR : ").grid(row=0,column=0)
e1=Entry(root)
e1.grid(row=0,column=1)

Label(root,text="Enter the Choice 1.US Doller, 2. Pound, 3. Dirham").grid(row=1,column=0)
e2=Entry(root)
e2.grid(row=1,column=1)

Button(root,text="Submit",command=submit).grid(row=3,column=3)
