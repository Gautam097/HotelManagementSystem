# Creating a login page

from cProfile import label
from email import message
from email.mime import image
from struct import pack
from sys import maxsize
from tkinter import *
from tkinter import messagebox
from turtle import bgcolor, dot, title, width
import tkinter.font as TkFont
import cx_Oracle
from PIL import Image,ImageTk

from manager_page import manage


# It will Take you to the manager page 
def manager():
    from manager_page import manage
    root1=Toplevel()
    ob2=manage(root1)
    root1.mainloop()

# It will take you to the registration Page
def registration():
    from Register_form import Register
    root0=Toplevel()
    ob1=Register(root0)

    root0.mainloop()
    # Register(root0)
    
# oracle connection
def connect():
    con=cx_Oracle.connect('cinema/danish30')
    print(con.version)
    cursor=con.cursor()
    return cursor


# Cancel function
def cancel():
    check=messagebox.askquestion("Permsission",'Do you Really Want to Exit')
    if(check=='yes'):
        root.destroy()



# Login function 
def login():
    u_name=user_name.get()
    u_pass=user_password.get()
    flag=-1
    
    # checking if fields are empty or not 
    if u_name=="" and u_pass=="":
        messagebox.showwarning('Login Error','Username And Password Required')

    # checking if MANAGER has acess the system
    elif u_name=='manager' and u_pass=="man123":
        print('manager has acessed the system')
        manager()
        
        
    # Creting or checking a customer 
    elif u_name!="" and u_pass!="":
        # con=cx_Oracle.connect('cinema/danish30')
        # print(con.version)
        # cursor=con.cursor()
        # cursor.execute('select * from password')
        # l=cursor.fetchall()
        user_cursor=connect()
        user_cursor.execute('select * from password')
        l=user_cursor.fetchall()
        for i in l:
        #checking the USERNAME in the database 
            if(u_name==i[0]) and(u_pass==i[1]):
                flag=1
                break
        if(flag==1):
            print("Customer Page")
        #  if username is not in the database then go to registration page
        else:
            user_check=messagebox.showerror('User Error','USER NOT FOUND')
            a=messagebox.askquestion('REGISTER','WANT TO REGISTER')
            if(a=='yes'):
                # Going to Registration page
                registaration()
                
                
                
                
            
        


root=Tk()
root.geometry('1255x944+136+0')
root.title("LOGIN PAGE")
root.minsize(1255,944)
root.maxsize(1255,944)
# root.resizable(0,0)
# "magneto",30,"bold"

font=TkFont.Font(family="Bold",weight="bold")
# title_font=TkFont.Font(family="Comic Sans MS",weight="bold")
title_font=("Arial Greek",30,"bold","italic")





login_image=ImageTk.PhotoImage(Image.open('login_bg.jpg'))
login_label=Label(root,image=login_image).place(x=0,y=0,relwidth=1,relheight=1)

# CANVAS PORTION
# login_canvas=Canvas(root,width=200,height=200)
# login_icon=PhotoImage(file="b.png")
# login_canvas.create_image((130,150),image=login_icon)
# login_canvas.pack()


login_frame=Frame(root,bd=10,borderwidth=7,relief=RAISED)
login_frame.place(x=430,y=340)
login_frame_img=ImageTk.PhotoImage(Image.open('Blur.jpg'))
login_frame_label=Label(login_frame,image=login_frame_img)
login_frame_label.place(anchor='center')

# Title frame
title_frame=Frame(root)
title_frame.pack()
title_text=Label(title_frame,text='Welcome To AGC Cinema',font=("magneto",30,"bold"),bd=5,borderwidth=13,bg='#7d1515',relief=RAISED)
title_text.pack()

# Username and Passwords inputs
username=Label(login_frame,text='USERNAME :-',relief=RAISED,font=("magneto",12,"bold"),bg='#6f747d',bd=4,width=12)
password=Label(login_frame,text='PASSWORD :-',relief=RAISED,font=("magneto",12,"bold"),bg='#6f747d',bd=4,width=12)

user_name=Entry(login_frame,border=5,width=30,borderwidth=4,bg='#7d1515',relief=RIDGE,fg='white',font=("times",9,"bold"))
user_password=Entry(login_frame,border=5,width=30,show='*',bg='#7d1515',relief=RIDGE,fg='white',font=("times",9,"bold"))

username.grid(row=0,column=0,pady=10)
password.grid(row=1,column=0)
user_name.grid(row=0,column=1,padx=20)
user_password.grid(row=1,column=1,padx=10,columnspan=2)

# creating LOGIN button
login_button=Button(login_frame,text='Login',border=5,borderwidth=5,width=10,bg='#5e6269',font=("magneto",12,"bold"),command= login)
login_button.grid(row=2,column=1,pady=10)

# Creating Cancel Button
cancel_button=Button(login_frame,text='Cancel',border=5,borderwidth=5,width=10,bg='#ad1a1a',font=("magneto",12,"bold"),command=cancel)
cancel_button.grid(row=3,column=1)




root.mainloop()