from tkinter import *
from tkinter import font
from tkinter import ttk
from tkinter import font
from turtle import width
import tkinter.messagebox as tmsg
from PIL import Image ,ImageTk
from setuptools import Command   
import cx_Oracle

class reg:
    
    def __init__(self,winregister):
        # print("hello")
        self.win=winregister
        self.win.title("Register Here")
        self.win.geometry("1600x1500")

        #=============== first Image =============
        img1= Image.open("117.jpg")
        img1=img1.resize((1600,1500))
        self.photoimg1= ImageTk.PhotoImage(img1)

        lblimg = Label(self.win,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=1500)


        
        # variable to be used in the registration form
        self.username=StringVar()
        self.password=StringVar()
        self.age=StringVar()
        self.number=StringVar()


        title=Label(self.win,text="REGISTER HERE",font=("lucida 20 bold"))
        title.pack()

        
        frame = Frame(self.win,bd=10)
        frame.place(x=400,y=100,width=800,height=600)

        #=============== frame Image =============
        img2= Image.open("111.jpg")
        img2=img2.resize((800,600))
        self.photoimg2= ImageTk.PhotoImage(img2)

        lblimg = Label(frame,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=800,height=600)



        l1 = Label(frame,bd=10,text="Name",relief=SUNKEN,font="lucida 20 bold")
        l1.place(x=0,y=50,height=50,width=100)

        l2  = Label(frame,bd=10,text="Mobile No",relief=SUNKEN,font="lucida 20 bold")
        l2.place(x=0,y=150,height=50,width=180)

        l3  = Label(frame,bd=10,text="Age",relief=SUNKEN,font="lucida 20 bold")
        l3.place(x=0,y=250,height=50,width=100)

        l4  = Label(frame,bd=10,text="Password",relief=SUNKEN,font="lucida 20 bold")
        l4.place(x=0,y=350,height=50,width=180)

        username = Entry(frame,bd=10,textvariable=self.username,relief=SUNKEN,font="lucida 20 bold")
        username .place(x=200,y=50,width=500,height=50)

        number  = Entry(frame,bd=10,textvariable=self.number,relief=SUNKEN,font="lucida 20 bold")
        number.place(x=200,y=150,width=500,height=50)

        age  = Entry(frame,bd=10,textvariable=self.age,relief=SUNKEN,font="lucida 20 bold")
        age.place(x=200,y=250,width=500,height=50)

        password  = Entry(frame,bd=10,textvariable=self.password,relief=SUNKEN,font="lucida 20 bold")
        password.place(x=200,y=350,width=500,height=50)


        b1=Button(frame,text ="Register Here",command=self.register,relief=SUNKEN,font="lucida 20 bold",bd=10)
        b1.place(x=200,y=450,height=50,width=400)

        b1=Button(frame,text ="GO Back",command=self.win.destroy,relief=SUNKEN,font="lucida 20 bold",bd=10)
        b1.place(x=200,y=500,height=50,width=400)


        self.win=mainloop()

    def register(self):
        
        if self.username.get()=="" or self.number.get()=="" or self.age.get()=="" or self.password.get()=="":
            tmsg.showerror("Error","Plzz fill all field it's mandatory",parent= self.win)

        else:
            u=self.username.get()
            m=self.number.get()
            a=self.age.get()
            p=self.password.get()
            

            # Conneting to the database
            conn= cx_Oracle.connect("gautam/gautam123")
            print(conn.version)
            # create cursor
            c = conn.cursor()

            try:
                c.execute("Insert into registration values(:1,:2,:3,:4)",(u,m,a,p))
                c.execute("insert into password values(:1,:4)",(u,p))

            except cx_Oracle.IntegrityError:
                tmsg.messagebox.showerror("EXISTED","CUSTOMER ALREADY EXISTED")

            else:
                # commit changes
                conn.commit()

                # close database connection
                conn.close()
                a=tmsg.showinfo("REGISTER HERE","you are registered successfully")
                if(a=="ok"):
                    self.win.exit()
                # if(a=="ok"):
                #     b=tmsg.askyesno("permission","GO TO LOGIN PAGE")
                #     if(b=="yes"):
                #         self.win.exit()
                #     # else:
                    #     tmsg.showinfo("go to","go to sign up page")











            


        
    
if __name__=="__main__":
    root=Tk() # tk means toolkit
    obj= reg(root)
    root.mainloop()