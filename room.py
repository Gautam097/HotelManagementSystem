from codeop import CommandCompiler
import email
import imp
from tkinter import *
from tkinter import font
from tkinter.ttk import Labelframe
from turtle import width
from unittest.main import main
from wsgiref import validate
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox
import cx_Oracle
from time import strftime
from datetime import datetime


class roombook:
    def __init__(self,gautam):
        self.root= gautam
        self.root.title("For Room booking")
        self.root.geometry("1295x550+230+220")


        # variable to be used to store in database
        self.ref= StringVar()
        self.checkin= StringVar()
        self.checkout= StringVar()
        self.roomtype= StringVar()
        self.roomavailable= StringVar()
        self.meal= StringVar()
        self.noOfdays= StringVar()
        self.paidtax= StringVar()
        self.actualtotal= StringVar()
        self.total1= StringVar()


        # ==================== Title image ============
        lbl_title= Label(self.root,text="ADD ROOM DETAILS",font="lucida 18 bold",bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)



        # =================== logo image =============
        img2= Image.open("112.jpg")
        img2=img2.resize((100,40))
        self.photoimg2= ImageTk.PhotoImage(img2)

        lblimg = Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=3,width=100,height=40)


        # =====================Label frame =================
        labelframeleft = LabelFrame(self.root,relief=RIDGE,text="Roombooking Details",font="lucida 12 bold",bd=4,padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)

        #====================labels and entry=============
        # cust ref
        lbl_cust_ref=Label (labelframeleft,text="Customer Ref",font="lucida 12 bold",padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0)

        ref=ttk.Entry(labelframeleft,textvariable=self.ref,width=15,font="lucida 12 bold")
        ref.grid(row=0,column=1,sticky='w')

        # fetch data button
        btnfetch=Button(labelframeleft,text="Fetch Data",command=self.Fetch_ref,font="lucida 12 bold",bg="black",fg="gold",width=8)
        btnfetch.place(x=300,y=4)


        # check in date
        lblcheckin=Label (labelframeleft,text="check_in_date",font="lucida 12 bold",padx=2,pady=6)
        lblcheckin.grid(row=1,column=0)

        txt_checkin=ttk.Entry(labelframeleft,textvariable=self.checkin,width=29,font="lucida 12 bold")
        txt_checkin.grid(row=1,column=1,sticky='w')

        # check out date
        lblcheckout=Label (labelframeleft,text="check_out_date",font="lucida 12 bold",padx=2,pady=6)
        lblcheckout.grid(row=2,column=0)

        txt_checkout=ttk.Entry(labelframeleft,textvariable=self.checkout,width=29,font="lucida 12 bold")
        txt_checkout.grid(row=2,column=1,sticky='w')

        # room type
        lbl_roomtype=Label (labelframeleft,text="Room Type",font="lucida 12 bold",padx=2,pady=6)
        lbl_roomtype.grid(row=3,column=0)

        
        # txt_roomtype=ttk.Entry(labelframeleft,textvariable=self.roomtype,width=29,font="lucida 12 bold")
        # txt_roomtype.grid(row=3,column=1,sticky='w')

        # Connecting to the DATABASE
        con=cx_Oracle.connect('gautam/gautam123')
        # print(con.version)
        my_cursor=con.cursor()
        my_cursor.execute("select roomno from  add_room")
        rows= my_cursor.fetchall()

        combo_roomtype=ttk.Combobox(labelframeleft,font="lucida 12 bold",textvariable=self.roomtype,width=27,state="readonly")
        combo_roomtype["value"]=rows
        combo_roomtype.current(0)
        combo_roomtype.grid(row=3,column=1)



        # available room
        lblavailable_room=Label (labelframeleft,text="Available Room",font="lucida 12 bold",padx=2,pady=6)
        lblavailable_room.grid(row=4,column=0)

        # txt_available_room=ttk.Entry(labelframeleft,textvariable=self.roomavailable,width=29,font="lucida 12 bold")
        # txt_available_room.grid(row=4,column=1,sticky='w')

        # Connecting to the DATABASE
        con=cx_Oracle.connect('gautam/gautam123')
        # print(con.version)
        my_cursor=con.cursor()
        my_cursor.execute("select roomtype from  add_room")
        rows2= my_cursor.fetchall()


        combo_roomtype=ttk.Combobox(labelframeleft,font="lucida 12 bold",textvariable=self.roomavailable,width=27,state="readonly")
        combo_roomtype["value"]=rows2
        combo_roomtype.current(0)
        combo_roomtype.grid(row=4,column=1)


        # Meal
        lblmeal=Label (labelframeleft,text="Meal",font="lucida 12 bold",padx=2,pady=6)
        lblmeal.grid(row=5,column=0)

        txt_meal=ttk.Entry(labelframeleft,textvariable=self.meal,width=29,font="lucida 12 bold")
        txt_meal.grid(row=5,column=1,sticky='w')
        # Number of days
        lbl_nos_of_days=Label (labelframeleft,text="Number of days:",font="lucida 12 bold",padx=2,pady=6)
        lbl_nos_of_days.grid(row=6,column=0)

        txt_nosofdays=ttk.Entry(labelframeleft,textvariable=self.noOfdays,width=29,font="lucida 12 bold")
        txt_nosofdays.grid(row=6,column=1,sticky='w')

        # paid tax
        lblpaid_tax=Label (labelframeleft,text="Paid tax",font="lucida 12 bold",padx=2,pady=6)
        lblpaid_tax.grid(row=7,column=0)

        # combo_nationality=ttk.Combobox(labelframeleft,font="lucida 12 bold",width=27,state="readonly")
        # combo_nationality["value"]=("Indian","American","Britist")
        # combo_nationality.current(0)
        # combo_nationality.grid(row=7,column=1)

        txt_paid_tax=ttk.Entry(labelframeleft,textvariable=self.paidtax,width=29,font="lucida 12 bold")
        txt_paid_tax.grid(row=7,column=1,sticky='w')





        # ==sub total====
        lblsub_total=Label (labelframeleft,text="Sub total",font="lucida 12 bold",padx=2,pady=6)
        lblsub_total.grid(row=8,column=0)

        # combo_idproof=ttk.Combobox(labelframeleft,font="lucida 12 bold",width=27,state="readonly")
        # combo_idproof["value"]=("Adhar card","Passport","Driving licence")
        # combo_idproof.current(0)
        # combo_idproof.grid(row=8,column=1)

        txt_sub_total=ttk.Entry(labelframeleft,textvariable=self.actualtotal,width=29,font="lucida 12 bold")
        txt_sub_total.grid(row=8,column=1,sticky='w')



        #================== total cost=========
        lbltotal_cost=Label (labelframeleft,text="Total cost",font="lucida 12 bold",padx=2,pady=6)
        lbltotal_cost.grid(row=9,column=0)

        txt_total_cost=ttk.Entry(labelframeleft,textvariable=self.total1,width=29,font="lucida 12 bold")
        txt_total_cost.grid(row=9,column=1,sticky='w')

        # # =================== bill button=================
        # btn_bill=Button(labelframeleft,text="Bill",command=self.total,font="lucida 12 bold",bg="black",fg="gold",width=8)
        # btn_bill.place(x=10,y=350)


        #=====================btn left frame==============
        btn_frame = Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add, font="lucida 12 bold",bg="black",fg="gold",width=9)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.update_btn,font="lucida 12 bold",bg="black",fg="gold",width=9)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.delete_btn,font="lucida 12 bold",bg="black",fg="gold",width=9)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.reset,font="lucida 12 bold",bg="black",fg="gold",width=9)
        btnReset.grid(row=0,column=3,padx=1)

        # right side image 

        img3= Image.open("2.jpg")
        img3=img3.resize((530,300))
        self.photoimg3= ImageTk.PhotoImage(img3)

        lblimg = Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
        lblimg.place(x=760,y=55,width=530,height=300)



        # ==================Label frame search system========================
        Table_frame = LabelFrame(self.root,relief=RIDGE,text="View Details",font="lucida 12 bold",bd=4,padx=2)
        Table_frame.place(x=435,y=280,width=860,height=260)

        # lblSearchBy=Label (Table_frame,text="Search By:",font="lucida 12 bold",bg="red",fg='white')
        # lblSearchBy.grid(row=0,column=0,sticky='w',padx=2)

        # # self.search_var=StringVar()
        # combo_Search=ttk.Combobox(Table_frame,font="lucida 12 bold",width=24,state="readonly")
        # combo_Search["value"]=("Ref","Room")
        # combo_Search.current(1)
        # combo_Search.grid(row=0,column=1)

        # # self.txt_search=StringVar()
        # txtSearch=ttk.Entry(Table_frame,width=24,font="lucida 12 bold")
        # txtSearch.grid(row=0,column=2,padx=2)


        # btnSearch=Button(Table_frame,text="Search",font="lucida 12 bold",bg="black",fg="gold",width=9)
        # btnSearch.grid(row=0,column=3,padx=1)


        # btnShowall=Button(Table_frame,text="Show All",font="lucida 12 bold",bg="black",fg="gold",width=9)
        # btnShowall.grid(row=0,column=4,padx=1)


        #====================== show data table =======================
        room_details_table = Frame(Table_frame,bd=2,relief=RIDGE)
        room_details_table.place(x=0,y=50,width=860,height=180)

        scroll_x=ttk.Scrollbar(room_details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(room_details_table,orient=VERTICAL)

        self.room_details_table= ttk.Treeview(room_details_table,columns=("ref","checkin","checkout","roomtype","roomavailable","meal","noOfdays"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_details_table.xview)
        scroll_y.config(command=self.room_details_table.yview)

        self.room_details_table.heading("ref",text="Refer NO")
        self.room_details_table.heading("checkin",text="check-in")
        self.room_details_table.heading("checkout",text="check_out")
        self.room_details_table.heading("roomtype",text="Room Type")
        self.room_details_table.heading("roomavailable",text="Room NO")
        self.room_details_table.heading("meal",text="Meal")
        self.room_details_table.heading("noOfdays",text="NoOfDays")

        self.room_details_table["show"]="headings"

        self.room_details_table.column("ref",width=100)
        self.room_details_table.column("checkin",width=100)
        self.room_details_table.column("checkout",width=100)
        self.room_details_table.column("roomtype",width=100)
        self.room_details_table.column("roomavailable",width=100)
        self.room_details_table.column("meal",width=100)
        self.room_details_table.column("noOfdays",width=100)

        
        self.room_details_table.pack(fill=BOTH,expand=1)

        self.room_details_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    # =============///  all data fetch which is at customer page //////======
    def Fetch_ref(self):
        if self.ref.get()=="":
            messagebox.showerror("Error","please enter reference number",parent=self.root)

        else:
             # Connecting to the DATABASE for cname
            con=cx_Oracle.connect('gautam/gautam123')
            # print(con.version)
            cursor=con.cursor()
            cursor.execute("select cname from customer where ref="+self.ref.get())
            
            row= cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","this ref number is not found",parent=self.root)

            else:
                con.commit()
                con.close()
            
                showDataframe= Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataframe.place(x=455,y=55,width=300,height=200)

                lblName=Label(showDataframe,text="Name:",font="lucida 12 bold")
                lblName.place(x=0,y=0)

                lbl=Label(showDataframe,text=row,font="lucida 12 bold")
                lbl.place(x=90,y=0)

                 # Connecting to the DATABASE for gender
                con=cx_Oracle.connect('gautam/gautam123')
                # print(con.version)
                cursor=con.cursor()
                cursor.execute("select gender from customer where ref="+self.ref.get())

                row= cursor.fetchone()

                lblGender=Label(showDataframe,text="gender:",font="lucida 12 bold")
                lblGender.place(x=0,y=30)

                lbl2=Label(showDataframe,text=row,font="lucida 12 bold")
                lbl2.place(x=90,y=30)

                 # Connecting to the DATABASE for idproof
                con=cx_Oracle.connect('gautam/gautam123')
                # print(con.version)
                cursor=con.cursor()
                cursor.execute("select idproof from customer where ref="+self.ref.get())

                row= cursor.fetchone()

                lblGender=Label(showDataframe,text="Id proof:",font="lucida 12 bold")
                lblGender.place(x=0,y=60)

                lbl2=Label(showDataframe,text=row,font="lucida 12 bold")
                lbl2.place(x=90,y=60)

                 # Connecting to the DATABASE  for id number
                con=cx_Oracle.connect('gautam/gautam123')
                # print(con.version)
                cursor=con.cursor()
                cursor.execute("select idnum from customer where ref="+self.ref.get())

                row= cursor.fetchone()

                lblGender=Label(showDataframe,text="Id num:",font="lucida 12 bold")
                lblGender.place(x=0,y=90)

                lbl2=Label(showDataframe,text=row,font="lucida 12 bold")
                lbl2.place(x=90,y=90)


                 # Connecting to the DATABASE  for address
                con=cx_Oracle.connect('gautam/gautam123')
                print(con.version)
                # cursor=con.cursor()
                cursor.execute("select addrr from customer where ref="+self.ref.get())

                row= cursor.fetchone()

                lblGender=Label(showDataframe,text="address:",font="lucida 12 bold")
                lblGender.place(x=0,y=120)

                lbl2=Label(showDataframe,text=row,font="lucida 12 bold")
                lbl2.place(x=90,y=120)


                 # Connecting to the DATABASE  postcode 
                con=cx_Oracle.connect('gautam/gautam123')
                # print(con.version)
                cursor=con.cursor()
                cursor.execute("select postcode from customer where ref="+self.ref.get())

                row= cursor.fetchone()

                lblGender=Label(showDataframe,text="postcode:",font="lucida 12 bold")
                lblGender.place(x=0,y=150)

                lbl2=Label(showDataframe,text=row,font="lucida 12 bold")
                lbl2.place(x=90,y=150)

    # add data into room
    def add(self):
        if self.ref.get()=="":
            messagebox.showerror("Error","pleae fil reference boxes")

        else:
            r= self.ref.get()
            cn= self.checkin.get()
            co=self.checkout.get()
            rt= self.roomtype.get()
            ra= self.roomavailable.get()
            m= self.meal.get()
            d= self.noOfdays.get()
            pt= self.paidtax.get()
            at= self.actualtotal.get()
            t= self.total1.get()


             # Connecting to the DATABASE
            con=cx_Oracle.connect('gautam/gautam123')
            # print(con.version)
            cursor=con.cursor()
            try:
                cursor.execute("INSERT INTO ROOM VALUES(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10)",(r,cn,co,rt,ra,m,d,pt,at,t))    
            except cx_Oracle.IntegrityError:
                messagebox.showerror("ALREADY EXISTED","CUSTOMER ALREADY EXISTED",parent=self.root)
            
            else:
                con.commit()
                self.fetch_data()
                con.close()
                a=messagebox.showinfo("COMPLETED","CUSTOMER ADDED SUCCESFULLY",parent=self.root)



    def reset(self):
        self.ref.set("")
        self.checkin.set("")
        self.checkout.set("")
        self.roomtype.set("")
        self.roomavailable.set("")
        self.meal.set("")
        self.noOfdays.set("")
        self.paidtax.set("")
        self.actualtotal.set("")
        self.total1.set("")


    # ==========///// Fetch Data /////////==========
    def fetch_data(self):
        # Connecting to the DATABASE
        con=cx_Oracle.connect('gautam/gautam123')
        # print(con.version)
        my_cursor=con.cursor()
        my_cursor.execute("select * from  room")
        rows= my_cursor.fetchall()
        if len(rows)!=0:
            self.room_details_table.delete(*self.room_details_table.get_children())

            for i in rows:
                self.room_details_table.insert("",END,values=i)

            con.commit()
        con.close()
        
        


    # ============== get cursor for updatation again /////////////////======
    def get_cursor(self,events=""):
        cursor_row= self.room_details_table.focus()
        content= self.room_details_table.item(cursor_row)
        row= content["values"]


        self.ref.set(row[0])
        self.checkin.set(row[1])
        self.checkout.set(row[2])
        self.roomtype.set(row[3])
        self.roomavailable.set(row[4])
        self.meal.set(row[5])
        self.noOfdays.set(row[6])
        self.paidtax.set(row[7])
        self.actualtotal.set(row[8])
        self.total1.set(row[9])




    def update_btn(self):
        if self.ref.get()=="":
            messagebox.showerror("Form","please fill reference number !!!!!",parent=self.root)
        else:
            r= self.ref.get()
            cn= self.checkin.get()
            co=self.checkout.get()
            rt= self.roomtype.get()
            ra= self.roomavailable.get()
            m= self.meal.get()
            d= eval(self.noOfdays.get())
            pt= self.paidtax.get()
            at= self.actualtotal.get()
            t= self.total1.get()

        # Connecting to the DATABASE
            con=cx_Oracle.connect('gautam/gautam123')
            # print(con.version)
            cursor=con.cursor()

            try:
                cursor.execute("UPDATE ROOM SET checkin =:2,checkout=:3,roomtype=:4,roomavai=:5,meal=:6,days=:7,paidtax=:8,actualtotal=:9,total1= :10 WHERE ref like '%s'"%r,(cn,co,rt,ra,m,d,pt,at,t))
                
                con.commit()
                self.fetch_data()  
                con.close()
            except cx_Oracle.IntegrityError:
                messagebox.showerror("ALREADY EXISTED","CUSTOMER ALREADY EXISTED IN THE LIST",parent=self.root)
            
            else:
                messagebox.showinfo("SUCCESS","RECORD UPDATED SUCCESFULLY",parent=self.root)


    # ===========/// Delete the records of room by ref number ///////===========
    def delete_btn(self):
        r=self.ref.get()
        if r=="":
            messagebox.showerror("Error","Ref number is Required to Delete the record!!",parent=self.root)
        else:
            con=cx_Oracle.connect("gautam/gautam123")
            cur=con.cursor()
            cur.execute("Delete From room where ref = :id",id=r)
            #rows = cur.fetchall()
            con.commit()
            self.fetch_data()
            con.close()
            messagebox.showinfo("Success","Record Deleted Successfully",parent=self.root)


    def total(self):
        inDate = self.checkin.get()
        outDate = self.checkout.get()

        inDate=datetime.strptime(inDate,"%D/%m/%y")
        outDate=datetime.strptime(outDate,"%D/%m/%y")

        self.noOfdays.set(abs(outDate-inDate).days)


if __name__=="__main__":
    roombook_win=Tk()
    obj2=roombook(roombook_win)
    roombook_win.mainloop()
