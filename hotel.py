import imp
import re
from tkinter import *
from turtle import width
from unittest.main import main
from PIL import Image,ImageTk
from customer import Cust_win
# from add_room import Add_room_win
from tkinter import messagebox


class HotelManagementSystem:
    def __init__(self,root):
        self.root= root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")

        #=============== first Image =============
        img1= Image.open("117.jpg")
        img1=img1.resize((1550,140))
        self.photoimg1= ImageTk.PhotoImage(img1)

        lblimg = Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)

        # =================== logo image =============
        img2= Image.open("113.jpg")
        img2=img2.resize((230,140))
        self.photoimg2= ImageTk.PhotoImage(img2)

        lblimg = Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=230,height=140)


        # ==================== Titel image ============
        lbl_title= Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font="lucida 40 bold",bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)

        # ==================== main frame ==============
        main_frame= Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550 ,height=620)

        #==================== menu ===================
        lbl_menu= Label(main_frame,text="ALL MENU",font="lucida 20 bold",bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)

        #=====================button frame =============
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=228,height=190)

        cust_btn=Button(btn_frame,text="ADD CUSTOMER",command=self.cust_details,font="lucida 14 bold",bg="black",fg="gold",bd=0,width=22,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn=Button(btn_frame,text="DETAILS OF ROOM",command=self.room_details,font="lucida 14 bold",bg="black",fg="gold",bd=0,width=22,cursor="hand1")
        room_btn.grid(row=1,column=0,pady=1,sticky="w")

        details_btn=Button(btn_frame,text="ADD ROOM",command=self.addroom_details,font="lucida 14 bold",bg="black",fg="gold",bd=0,width=22,cursor="hand1")
        details_btn.grid(row=2,column=0,pady=1)

        report_btn=Button(btn_frame,text="SHOW ALL GUEST",command=self.show,font="lucida 14 bold",bg="black",fg="gold",bd=0,width=22,cursor="hand1")
        report_btn.grid(row=3,column=0,pady=1)

        logout_btn=Button(btn_frame,text="LOG OUT",command=self.logout,font="lucida 14 bold",bg="black",fg="gold",bd=0,width=22,cursor="hand1")
        logout_btn.grid(row=4,column=0,pady=1)

        #================ right side Image ================
        img3= Image.open("10.png")
        img3=img3.resize((1310,590))
        self.photoimg3= ImageTk.PhotoImage(img3)

        lblimg = Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg.place(x=225,y=0,width=1310,height=590)


        # ===================== down images==============
        img4= Image.open("114.jpg")
        img4=img4.resize((230,210))
        self.photoimg4= ImageTk.PhotoImage(img4)

        lblimg = Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=225,width=230,height=210)

        img5= Image.open("112.jpg")
        img5=img5.resize((230,210))
        self.photoimg5= ImageTk.PhotoImage(img5)

        lblimg = Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=420,width=230,height=190)

    def cust_details(self):
        self.new_window= Toplevel(self.root)
        self.app=Cust_win(self.new_window)

    def room_details(self):
        
        from room import roombook
        self.room = Toplevel(self.root)
        self.gautam= roombook(self.room)

    def addroom_details(self):
        
        from add_room import Add_room_win
        self.adding_room = Toplevel(self.root)
        self.room_win= Add_room_win(self.adding_room)

    def logout(self):
        check=messagebox.askquestion("Permsission",'Do you Really Want to Exit',parent=self.root)
        if(check=='yes'):
            self.root.destroy()
    

    def show(self):
        from show_details import showdetails
        self.show_all = Toplevel(self.root)
        self.showdetail_win = showdetails(self.show_all)



if __name__=="__main__":
    root=Tk() # tk means toolkit
    obj= HotelManagementSystem(root)
    root.mainloop()