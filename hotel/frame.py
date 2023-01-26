from msilib.schema import Font
from pydoc import text
from tkinter import * 
root= Tk()
root.geometry("1600x1400")
root.title("welcome to gautam gui ")
f1 =Frame(root,borderwidth=6,bg="grey")
f1.place(x=800,y=300,width=450,height=350)

label1=Label(f1,text ="Hotel management system")
label1.pack(side=TOP,fill=X)

f2= Frame(root,borderwidth=8,bg= "aqua")
f2.place(x=0,y=50,width=200,height=900)

lable2=Label(f2,text="Grand Hotel Menu")
lable2.pack(side=TOP,fill=X)

f3=Frame(root,bg="red")
f3.place(x=500,y=80,width=900,height=100)

label3=Label(f3,text="welcome to the grand Hotel", font="Helvetica 50 bold")
label3.pack(side=TOP,padx=20,pady=20)

b1=Button(f2,text="check room avaibility",bg="pink")
b1.place(x=0,y=100,height=50)

b1=Button(f2,text="Main menu",bg="green")
b1.place(x=0,y=200,height=50)

b1=Button(f2,text="Book your meal",bg="yellow")
b1.place(x=0,y=300,height=50)

b1=Button(f2,text="know about food services",bg="blue")
b1.place(x=0,y=400,height=50)

b1=Button(f2,text="log out window",bg="brown")
b1.place(x=0,y=500,height=50)

user=Label(f1,text="Enter your Name")
user.place(x=0,y=100)

password=Label(f1,text="Enter your password")
password.place(x=0,y=200)

user_in=Entry(f1)
user_in.place(x=200,y=100)

password_in=Entry(f1)
password_in.place(x=200,y=200)

b2=Button(f1,text="login here",bg="blue")
b2.place(x=100,y=500,height=100)






root.mainloop()
