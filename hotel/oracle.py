from tkinter import *
from tkinter import messagebox as tmsg 
from tkinter import font 
from PIL import Image,ImageTk
import cx_Oracle

root=Tk()
root.geometry("1600x1500")


#oracle connection
def connect():
    con=cx_Oracle.connect("scott/tiger")
    print(con.version)
    cursor=con.cursor()
    return cursor

# cancel function
def cancel():
    check=tmsg.askquestion("permission","Do you Really want to Exit")
    if(check=='yes'):
        # quit
        root.destroy()

# login function
def login():
    u_name= user_name.get()
    u_pass= user_password.get()
    flag=-1

#checking if fields are empty or not
    if u_name=="" and u_pass=="":
        tmsg.showwarning("login error","Username And Password Required")

    elif u_name=='gautam' and u_pass=="gautam123":
        password_cursor= connect()

    # creating or checking a customer
    elif u_name !="" and u_pass!= "":
        user_cursor=connect()
        user_cursor.execute('select * from password')
        l=user_cursor.fetchall()
        for i in l:
        # checking the username in the database
            if(u_name==i[0]) and (u_pass==i[1]):
                flag=1
                break
        if ( flag==1):
            print("customer page")
        # if username is not in the database then go to registration page
        else:
            user_check = tmsg.showerror('user Error',"user not found")
            tmsg.askquestion('REGISTER','WANT TO REGISTER')

        # message. askquestion('registration','')

        
        #font= TkFont.font(family="bold",weight="bold")

        login_frame=LabelFrame(root,text="Login page",padx=130,pady=80,border=7,borderwidth=10,relief=RAISED)

        #username and passwords inputs
        username=Label(login_frame,text="USERNAME :-",relief=RIDGE,pady=3,bd=4)
        password =Label(login_frame,text="PASSWORD :-",relief=RIDGE,pady=3,bd=4)

        user_name=Entry(login_frame,border=5,width=30,borderwidth=4)
        user_password=Entry(login_frame,border=5,width=30,borderwidth=4)

        username.grid(row=0,column=0,pady=10)
        password.grid(row=1,column=0,pady=10)

        user_name.grid(row=0,column=1,padx=10)
        user_password.grid(row=0,column=1,padx=10,columnspan=2)

        # creating login button
        login_button = Button(login_frame,text="Login",border=5,borderwidth=5,width=10,command= login)
        login_button.grid(row=2,column=1,pady=10)


        cancel_button = Button(login_frame,text="cancel",border=5,borderwidth=5,width=10,command= cancel)
        cancel_button.grid(row=3,column=1)

        root.mainloop()