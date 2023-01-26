from tkinter import * 
from tkinter import ttk
from tkinter import font
from turtle import width
from tkinter import messagebox
from PIL import Image ,ImageTk   # pip install pillow


class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")


        self.bg=ImageTk.PhotoImage(file="")

        lb1_bg=Label(self.root,image=self.bg)
        lb1_bg.place(x=0,y=0,relwidth=1,relheight=1) 


        frame =Frame(self.root,bg ="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open("")
        img1=img1.resize(100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.photoImage(img1)
        lblimg1 = Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)


        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        #Label
        username=lb1=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.Place(x=40,y=180, width=270)

        password=lb1=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)


        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.Place(x=40,y=250, width=270)

        #============== Icon image =============
        img2=Image.open("")
        img2=img2.resize(25,25),Image.ANTIALIAS)
        self.photoimage2=ImageTk.photoImage(img2)
        lblimg1 = Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=323,width=25,height=25)


        img3=Image.open("")
        img3=img3.resize(25,25),Image.ANTIALIAS)
        self.photoimage3=ImageTk.photoImage(img3)
        lblimg1 = Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=395, width=25,height=25)

        # Login button
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="whitel",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        # register button
        registerbtn=Button(frame,text="New user register",font=("times new roman",10,"bold"),borderwidth=0,relief=RIDGE,fg="whitel",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=20,y=350,width=160)

        # forget password button
        forgetbtn=Button(frame,text="Forget password",font=("times new roman",10,"bold"),borderwidth=0,relief=RIDGE,fg="whitel",bg="black",activeforeground="white",activebackground="black")
        forgetbtn.place(x=20,y=380,width=160)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all field required")
        elif self.txtuser.get()=="gautam" and self.txtpass.get()=="gautam123":
            messagebox.showinfo("success","welcome to Hotel management system")
        else:
            messagebox.showerror("invalid","invalid username & password")
 
if __name__== "__main__":
    root=Tk()
    app=Login_window(root)
    root.mainloop()