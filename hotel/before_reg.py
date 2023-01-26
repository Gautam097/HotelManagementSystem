from tkinter import *
from PIL import Image ,ImageTk
root = Tk()
root.geometry("1200x1600")
root.title("REGISTER HERE")
root.configure(background="blue")

bg= ImageTk.PhotoImage(file="117.jpg")
label = Label(root,image=bg)
label.place(x=0,y=0,relheight=1,relwidth=1)

frame = Frame(root,bd=20,bg="red")
frame.place(x=400,y=100,width=800,height=600)

l1 = Label(frame,bd=10,text="Name",relief=SUNKEN,font="lucida 20 bold")
l1.place(x=0,y=50,height=50,width=100)

l2  = Label(frame,bd=10,text="Mobile No",relief=SUNKEN,font="lucida 20 bold")
l2.place(x=0,y=150,height=50,width=180)

l3  = Label(frame,bd=10,text="Age",relief=SUNKEN,font="lucida 20 bold")
l3.place(x=0,y=250,height=50,width=100)

l4  = Label(frame,bd=10,text="Password",relief=SUNKEN,font="lucida 20 bold")
l4.place(x=0,y=350,height=50,width=180)

e1 = Entry(frame,bd=10,textvariable="Name",relief=SUNKEN,font="lucida 20 bold")
e1.place(x=200,y=50,width=500,height=50)

e2  = Entry(frame,bd=10,textvariable="Mobileno",relief=SUNKEN,font="lucida 20 bold")
e2.place(x=200,y=150,width=500,height=50)

e3  = Entry(frame,bd=10,textvariable="age",relief=SUNKEN,font="lucida 20 bold")
e3.place(x=200,y=250,width=500,height=50)

e4  = Entry(frame,bd=10,textvariable="password",relief=SUNKEN,font="lucida 20 bold")
e4.place(x=200,y=350,width=500,height=50)


b1=Button(frame,text ="Register Here",relief=SUNKEN,font="lucida 20 bold",bd=10)
b1.place(x=200,y=450,height=50,width=400)

root.mainloop()
