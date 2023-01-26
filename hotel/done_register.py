from cProfile import label
from email import message
from email.mime import image
from errno import ESTALE
from shutil import register_unpack_format
from sqlite3 import DatabaseError, Row
from struct import pack
from sys import maxsize
from tkinter import *
from tkinter import messagebox
from turtle import bgcolor, dot, title, width
import tkinter.font as TkFont
import cx_Oracle
from PIL import Image,ImageTk
import tkinter as tk

class Register:
    def _init_(self,winregister):
        self.winregister=winregister
        self.winregister.title('Registartion page')
        self.winregister.geometry('1255x944+136+0')
        self.winregister.minsize(1255,944)
        self.winregister.maxsize(1255,944)
        self.label_font=TkFont.Font(family="Bold",weight="bold")

       
        
        # Variables to be used to store users info
        self.username=StringVar()
        self.password=StringVar()
        self.gender=StringVar()
        self.age=StringVar()
        self.number=StringVar()

        self.login_image=ImageTk.PhotoImage(Image.open('login_bg.jpg'))
        login_label=Label(self.winregister,image=self.login_image)
        login_label.place(x=0,y=0,relwidth=1,relheight=1)

        # Creating a Registration Frame
        register_frame=Frame(self.winregister)
        register_frame.place(x=400,y=340,width=460,height=315)
        self.register_frame_image=ImageTk.PhotoImage(Image.open('Blur.jpg'))
        register_frame_label=Label(register_frame,image=self.register_frame_image)
        register_frame_label.place(x=0,y=0,relwidth=1,relheight=1)
        
         # Registration Title
        title_frame=Frame(self.winregister)
        title_frame.pack()
        registration_text=Label(title_frame,text='Registration Page',font=("magneto",30,"bold"),bd=5,borderwidth=13,bg='#7d1515',relief=RAISED)
        registration_text.pack()



        # Creating fields for inputs
        register_frame.columnconfigure(0,weight=3)
        register_frame.columnconfigure(1,weight=3)
        
        user_name=Label(register_frame,text='USERNAME :-',font=("magneto",12,"bold"),bd=5,relief=RAISED,bg='#6f747d',width=12)
        user_name.grid(row=0,column=0,padx=0,pady=14)

        user_name_entry=Entry(register_frame,textvariable=self.username,width=30,relief=RIDGE,bg='#7d1515',bd=5,fg='white',cursor='arrow',font=("times",10,"bold"))
        user_name_entry.grid(row=0,column=1,padx=5,pady=5)

        user_password=Label(register_frame,text='PASSWORD :-',font=("magneto",12,"bold"),bd=5,relief=RAISED,bg='#6f747d',width=12)
        user_password.grid(row=1,column=0,padx=0,pady=8)

        user_password_entry=Entry(register_frame,textvariable=self.password,width=30,relief=RIDGE,bg='#7d1515',bd=5,fg='white',font=("times",10,"bold"))
        user_password_entry.grid(row=1,column=1,padx=5,pady=5)

        user_gender=Label(register_frame,text='GENDER :-',font=("magneto",12,"bold"),bd=5,relief=RAISED,bg='#6f747d',width=12)
        user_gender.grid(row=2,column=0,pady=8)
        
        user_gender_entry=Entry(register_frame,textvariable=self.gender,width=30,relief=RIDGE,bg='#7d1515',bd=5,fg='white',font=("times",10,"bold"))
        # user_gender_entry.insert(0,'male or female')
        user_gender_entry.grid(row=2,column=1,padx=5,pady=5)
        
        user_age=Label(register_frame,text='AGE :-',font=("magneto",12,"bold"),bd=5,relief=RAISED,bg='#6f747d',width=12)
        user_age.grid(row=3,column=0,pady=8)

        user_age_entry=Entry(register_frame,textvariable=self.age,width=30,relief=RIDGE,bg='#7d1515',bd=5,fg='white',font=("times",10,"bold"))
        user_age_entry.grid(row=3,column=1,padx=5,pady=5)

        user_number=Label(register_frame,text='MOBILE_NO :-',font=("magneto",12,"bold"),bd=5,relief=RAISED,bg='#6f747d',width=12)
        user_number.grid(row=4,column=0,pady=8)

        user_number_entry=Entry(register_frame,textvariable=self.number,width=30,relief=RIDGE,bg='#7d1515',bd=5,fg='white',font=("times",10,"bold"))
        user_number_entry.grid(row=4,column=1,padx=5,pady=5)

        submit_button=Button(register_frame,text='SUBMIT',bd=6,borderwidth=9,bg='#5e6269',command=self.submit_data,width=15,font=("magneto",12,"bold"))
        submit_button.grid(row=5,column=1,padx=5,pady=5)



        self.winregister=mainloop()    

    def submit_data(self):
        if self.username.get()=="" or self.password.get()=="" or self.gender.get()=="" or self.age.get()=="" or self.number.get()=="":
            messagebox.showerror("Error","All (*) Fields Are Required!!!",parent=self.winregister)
            
        else:
            u=self.username.get()
            p=self.password.get()
            g=self.gender.get()
            a=self.age.get()
            m=self.number.get()
            
            # Connecting to the DATABASE
            con=cx_Oracle.connect('cinema/danish30')
            print(con.version)
            cursor=con.cursor()
            try:

                 cursor.execute("INSERT INTO REGISTRATION VALUES(:1,:2,:3,:4,:5)",(u,p,g,a,m))
                 cursor.execute("INSERT INTO PASSWORD VALUES(:1,:2)",(u,p))
           
            except cx_Oracle.IntegrityError:
                messagebox.showerror("ALREADY EXISTED","CUSTOMER ALREADY EXISTED")

            else:
                con.commit()
                con.close()
                a=messagebox.showinfo("COMPLETED","REGISTRATION SUCCESFUL")
                if (a=='ok'):
                    b=messagebox.askyesno("PERMISSION","GO BACK TO THE LOGIN PAGE")
                    if(b=='yes'):
                        self.winregister.quit()
                    
     
            
        


# root0=Toplevel()
# ob=Register(root0)
# root0.mainloop()

if __name__ =="main":    
    winregister=Tk()
    ob=Register(winregister)
    winregister.mainloop()