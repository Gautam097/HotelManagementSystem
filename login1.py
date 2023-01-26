from tkinter import *
from tkinter import font
from tkinter import ttk
from tkinter import font
from tokenize import String
from turtle import width
from tkinter import messagebox 
from PIL import Image ,ImageTk
from setuptools import Command   # pip install pillow
import cx_Oracle 


root= Tk()

root.geometry("1600x2000")
root.title("welcome to login system")

def main():
    from hotel import HotelManagementSystem
    root2=Toplevel()
    ob2=HotelManagementSystem(root2)
    root2.mainloop()

# oracle connection
def connect():
    con=cx_Oracle.connect('gautam/gautam123')
    cursor=con.cursor()
    return cursor

    

def rg():
    from register import reg
    root1=Toplevel()
    ob1=reg(root1)
    root1.mainloop()
    


# login function
def log_in():
    u_name=username.get()
    u_pass=u_password.get()
    flag=-1
    
    # checking if fields are empty or not 
    if u_name=="" and u_pass=="":
        messagebox.showwarning('Login Error','Username And Password Required')

    # checking if MANAGER has acess the system
    elif u_name=='manager' and u_pass=="gautam":
        print('manager has acessed the system')
        main()
        
        
    # Creating or checking a customer 
    elif u_name!="" and u_pass!="":
        
        user_cursor=connect()
        user_cursor.execute('select * from password')
        l=user_cursor.fetchall()
        for i in l:
        #checking the USERNAME in the database 
            if(u_name==i[0]) and(u_pass==i[1]):
                flag=1
                break
        if(flag==1):
            main()
        #  if username is not in the database then go to registration page
        else:
            user_check=messagebox.showerror('User Error','USER NOT FOUND')
            a=messagebox.askquestion('REGISTER','WANT TO REGISTER')
            if(a=='yes'):
                # Going to Registration page
                rg()

    
    
def forget():
    x=messagebox.showinfo("foget password","go to register page and register again")
    if (x=='ok'):
        rg()


bg=ImageTk.PhotoImage(file="112.jpg")
lb1_bg=Label(root,image=bg)
lb1_bg.place(x=0,y=0,relwidth=1,relheight=1) 

def rg():
    from register import reg
    root3=Toplevel()
    ob=reg(root3)
    root3.mainloop()


    
# variables to be used
username=StringVar()
u_password=StringVar()


# image = Image.open("login.png")
# photo = ImageTk.PhotoImage(image)

# label = Label(image=photo)
# label.place(x=800,y=100,width=200,height=100)

f1= Frame(root,relief=RAISED,bd=10,bg="black")
f1.place(x=500,y=100,width=800,height=650)

bg1=ImageTk.PhotoImage(file="111.jpg")
lb1_bg=Label(f1,image=bg1)
lb1_bg.place(x=0,y=0,relwidth=1,relheight=1) 


l1 = Label(f1,text="Login Here",bd=10,relief=SUNKEN,font="lucida 20 bold")
l1.pack(side=TOP,fill=X)

l3=Label(f1,text="Enter  your name ",bd=10,relief=SUNKEN,font="lucida 20 bold")
l3.place(x=0,y=100)

e1=Entry(f1,textvariable=username,bd=10,relief=SUNKEN,font="lucida 20 bold")
e1.place(x=0,y=150,height=50,width=350)

l4 =Label(f1,text="Enter  your password ",bd=10,relief=SUNKEN,font="lucida 20 bold")
l4 .place(x=0,y=250)

e2 =Entry(f1,textvariable=u_password,bd=10,relief=SUNKEN,font="lucida 20 bold",show="*")
e2 .place(x=0,y=300,height=50,width=350)

b1=Button(f1,text="Log In",command=log_in,bd=10,relief=SUNKEN,font="lucida 20 bold",cursor="hand1")
b1.place(x=10,y=400, height=50,width=150)

b2 =Button(f1,text="Register Here",bd=10,relief=SUNKEN,font="lucida 20 bold",command=rg,cursor="hand1")
b2 .place(x=200,y=400, height=50,width=300)

b3= Button(f1,text="Forget password",cursor="hand1",command=forget,bd=10,relief=SUNKEN,font="lucida 20 bold")
b3.place(x=0,y=500,height=50)

b4 = Button(f1,text="cancel",command=quit,bd=10,cursor="hand1",relief=SUNKEN,font="lucida 20 bold")
b4.place(x=0,y= 550,height=50)

root.mainloop()