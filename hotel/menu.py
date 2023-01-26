from tkinter import *
root= Tk()
root.geometry("1600x2000")
root.title("welcome to main menu")

f1= Frame(root,bd=10,bg="blue")
f1.place(x=0,y=0,width=200,height=200)

f2 = Frame(root,bd=10,bg="red")
f2.place(x=200,y=0,width=1400,height=200)

l2= Frame(root,bg="aqua",bd=10)
l2.place(x=0,y=200,width=1600,height=100)

f3= Frame(root,bd=10,bg="orange")
f3.place(x=0,y=300,width=400,height=2000)

f4 = Frame(root,bd=10,bg="red")
f4.place(x=200,y=0,width=1400,height=200)

f5= Frame(root,bd=10,bg="red")
f5.place(x=200,y=0,width=1400,height=200)

f6 = Frame(root,bd=10,bg="green")
f6.place(x=400,y=300,width=1400,height=2000)


root.mainloop()