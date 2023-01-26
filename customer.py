import email
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



class Cust_win:
    def __init__(self,root):
        self.root= root
        self.root.title("Hotel Management System")
        #width  x height + x + y
        self.root.geometry("1295x550+230+220")

        # variable to be used to store in database
        self.ref= StringVar()
        self.cname= StringVar()
        self.fname= StringVar()
        self.gender= StringVar()
        self.postcode= StringVar()
        self.mob= StringVar()
        self.email= StringVar()
        self.nationality= StringVar()
        self.idproof= StringVar()
        self.idnum= StringVar()
        self.addrr= StringVar()



        # ==================== Title image ============
        lbl_title= Label(self.root,text="ADD CUSTOMER DETAILS",font="lucida 18 bold",bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        # =================== logo image =============
        img2= Image.open("112.jpg")
        img2=img2.resize((100,40))
        self.photoimg2= ImageTk.PhotoImage(img2)

        lblimg = Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=3,width=100,height=40)


        # =====================Label frame =================
        labelframeleft = LabelFrame(self.root,relief=RIDGE,text="Customer Details",font="lucida 12 bold",bd=4,padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)

        #====================labels and entry=============
        # cust ref
        lbl_cust_ref=Label (labelframeleft,text="Customer Ref",font="lucida 12 bold",padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0)

        ref=ttk.Entry(labelframeleft,textvariable=self.ref,width=29,font="lucida 12 bold")
        ref.grid(row=0,column=1,sticky='w')

        # cust name
        lblcname=Label (labelframeleft,text="Customer Name",font="lucida 12 bold",padx=2,pady=6)
        lblcname.grid(row=1,column=0)

        cname=ttk.Entry(labelframeleft,textvariable=self.cname,width=29,font="lucida 12 bold")
        cname.grid(row=1,column=1,sticky='w')

        # father name
        lblmname=Label (labelframeleft,text="Father Name",font="lucida 12 bold",padx=2,pady=6)
        lblmname.grid(row=2,column=0)

        fname=ttk.Entry(labelframeleft,textvariable=self.fname,width=29,font="lucida 12 bold")
        fname.grid(row=2,column=1,sticky='w')

        # gender combobox
        label_gender=Label (labelframeleft,text="Gender",font="lucida 12 bold",padx=2,pady=6)
        label_gender.grid(row=3,column=0)

        # combo_gender=ttk.Combobox(labelframeleft,font="lucida 12 bold",width=27,state="readonly")
        # combo_gender["value"]=("Male","Female","Other")
        # combo_gender.current(0)
        # combo_gender.grid(row=3,column=1)

        gender=ttk.Entry(labelframeleft,textvariable=self.gender,width=29,font="lucida 12 bold")
        gender.grid(row=3,column=1,sticky='w')


        # postcode
        lblpostcode=Label (labelframeleft,text="Postcode",font="lucida 12 bold",padx=2,pady=6)
        lblpostcode.grid(row=4,column=0)

        postcode=ttk.Entry(labelframeleft,textvariable=self.postcode,width=29,font="lucida 12 bold")
        postcode.grid(row=4,column=1,sticky='w')

        # mobile number
        lblmobilenumber=Label (labelframeleft,text="Mob Number",font="lucida 12 bold",padx=2,pady=6)
        lblmobilenumber.grid(row=5,column=0)

        mob=ttk.Entry(labelframeleft,textvariable=self.mob,width=29,font="lucida 12 bold")
        mob.grid(row=5,column=1,sticky='w')
        # email
        lbl_email=Label (labelframeleft,text="E-mail",font="lucida 12 bold",padx=2,pady=6)
        lbl_email.grid(row=6,column=0)

        email=ttk.Entry(labelframeleft,textvariable=self.email,width=29,font="lucida 12 bold")
        email.grid(row=6,column=1,sticky='w')

        # nationality
        lblnationality=Label (labelframeleft,text="Nationality",font="lucida 12 bold",padx=2,pady=6)
        lblnationality.grid(row=7,column=0)

        # combo_nationality=ttk.Combobox(labelframeleft,font="lucida 12 bold",width=27,state="readonly")
        # combo_nationality["value"]=("Indian","American","Britist")
        # combo_nationality.current(0)
        # combo_nationality.grid(row=7,column=1)

        nationality=ttk.Entry(labelframeleft,textvariable=self.nationality,width=29,font="lucida 12 bold")
        nationality.grid(row=7,column=1,sticky='w')





        # id proof
        lblidproof=Label (labelframeleft,text="Id proof",font="lucida 12 bold",padx=2,pady=6)
        lblidproof.grid(row=8,column=0)

        # combo_idproof=ttk.Combobox(labelframeleft,font="lucida 12 bold",width=27,state="readonly")
        # combo_idproof["value"]=("Adhar card","Passport","Driving licence")
        # combo_idproof.current(0)
        # combo_idproof.grid(row=8,column=1)

        idproof=ttk.Entry(labelframeleft,textvariable=self.idproof,width=29,font="lucida 12 bold")
        idproof.grid(row=8,column=1,sticky='w')



        # id number
        lblidnumber=Label (labelframeleft,text="Id number",font="lucida 12 bold",padx=2,pady=6)
        lblidnumber.grid(row=9,column=0)

        idnum=ttk.Entry(labelframeleft,textvariable=self.idnum,width=29,font="lucida 12 bold")
        idnum.grid(row=9,column=1,sticky='w')

        # addresses
        lbladdress=Label (labelframeleft,text="Address",font="lucida 12 bold",padx=2,pady=6)
        lbladdress.grid(row=10,column=0)

        addrr=ttk.Entry(labelframeleft,textvariable=self.addrr,width=29,font="lucida 12 bold")
        addrr.grid(row=10,column=1,sticky='w')

        #=====================btn left frame==============
        btn_frame = Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_btn,font="lucida 12 bold",bg="black",fg="gold",width=9)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.update_btn,font="lucida 12 bold",bg="black",fg="gold",width=9)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.delete_btn,font="lucida 12 bold",bg="black",fg="gold",width=9)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.reset_btn,font="lucida 12 bold",bg="black",fg="gold",width=9)
        btnReset.grid(row=0,column=3,padx=1)

        # ==================Label frame search system========================
        Table_frame = LabelFrame(self.root,relief=RIDGE,text="View Details",font="lucida 12 bold",bd=4,padx=2)
        Table_frame.place(x=435,y=50,width=860,height=490)

        # lblSearchBy=Label (Table_frame,text="Search By:",font="lucida 12 bold",bg="red",fg='white')
        # lblSearchBy.grid(row=0,column=0,sticky='w',padx=2)

        # self.search_var=StringVar()
        # combo_Search=ttk.Combobox(Table_frame,textvariable=self.search_var,font="lucida 12 bold",width=24,state="readonly")
        # combo_Search["value"]=("Mobile","Ref")
        # combo_Search.current(0)
        # combo_Search.grid(row=0,column=1)

        # self.txt_search=StringVar()
        # txtSearch=ttk.Entry(Table_frame,textvariable=self.txt_search,width=24,font="lucida 12 bold")
        # txtSearch.grid(row=0,column=2,padx=2)


        # btnSearch=Button(Table_frame,text="Search",command=self.search_btn,font="lucida 12 bold",bg="black",fg="gold",width=9)
        # btnSearch.grid(row=0,column=3,padx=1)

        # btnShowall=Button(Table_frame,text="Show All",command=self.fetch_data,font="lucida 12 bold",bg="black",fg="gold",width=9)
        # btnShowall.grid(row=0,column=4,padx=1)

        #====================== show data table =======================
        cust_details_table = Frame(Table_frame,bd=2,relief=RIDGE)
        cust_details_table.place(x=0,y=50,width=860,height=350)

        scroll_x=ttk.Scrollbar(cust_details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(cust_details_table,orient=VERTICAL)

        self.cust_details_table= ttk.Treeview(cust_details_table,columns=("ref","name","father","gender","post","mobile","email","nationality","idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.cust_details_table.xview)
        scroll_y.config(command=self.cust_details_table.yview)

        self.cust_details_table.heading("ref",text="Refer NO")
        self.cust_details_table.heading("name",text="Name")
        self.cust_details_table.heading("father",text="Father Name")
        self.cust_details_table.heading("gender",text="Gender")
        self.cust_details_table.heading("post",text="Postcode")
        self.cust_details_table.heading("mobile",text="Mobile")
        self.cust_details_table.heading("email",text="Email")
        self.cust_details_table.heading("nationality",text="Nationality")
        self.cust_details_table.heading("idproof",text="Id proof")
        self.cust_details_table.heading("idnumber",text="Id number")
        self.cust_details_table.heading("address",text="Address")

        self.cust_details_table["show"]="headings"

        self.cust_details_table.column("name",width=100)
        self.cust_details_table.column("father",width=100)
        self.cust_details_table.column("gender",width=100)
        self.cust_details_table.column("post",width=100)
        self.cust_details_table.column("mobile",width=100)
        self.cust_details_table.column("email",width=100)
        self.cust_details_table.column("nationality",width=100)
        self.cust_details_table.column("idproof",width=100)
        self.cust_details_table.column("idnumber",width=100)
        self.cust_details_table.column("address",width=100)
        
        self.cust_details_table.pack(fill=BOTH,expand=1)

        self.cust_details_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    
    def add_btn(self):
        if self.ref.get()=="" or self.cname.get()=="" or self.fname.get()=="" or self.gender.get()=="" or self.postcode.get()=="" or self.mob.get()=="" or self.email.get()=="" or self.nationality.get()=="" or self.idproof.get()=="" or self.idnum.get()=="" or self.addrr.get()=="":
            messagebox.showerror("Error","All Fields Are Required!!!",parent=self.root)

        else:
            r=self.ref.get()
            c=self.cname.get()
            f=self.fname.get()
            g=self.gender.get()
            p=self.postcode.get()
            m=self.mob.get()
            e=self.email.get()
            n=self.nationality.get()
            i=self.idproof.get()
            id=self.idnum.get()
            a=self.addrr.get()

             # Connecting to the DATABASE
            con=cx_Oracle.connect('gautam/gautam123')
            print(con.version)
            cursor=con.cursor()
            try:
                cursor.execute("INSERT INTO customer VALUES(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11)",(r,c,f,g,p,m,e,n,i,id,a))    
            except cx_Oracle.IntegrityError:
                messagebox.showerror("ALREADY EXISTED","CUSTOMER ALREADY EXISTED",parent=self.root)
            
            else:
                con.commit()
                self.fetch_data()
                con.close()
                a=messagebox.showinfo("COMPLETED","CUSTOMER ADDED SUCCESFULLY",parent=self.root)

    def reset_btn(self):
        self.ref.set("")
        self.cname.set("")
        self.fname.set("")
        self.gender.set("")
        self.postcode.set("")
        self.mob.set("")
        self.email.set("")
        self.nationality.set("")
        self.idproof.set("")
        self.idnum.set("")
        self.addrr.set("")

    def showall_btn(self):
        pass


    # def fetch_data(self):
    #     # Connecting to the DATABASE
    #     con=cx_Oracle.connect('gautam/gautam123')
    #     print(con.version)
    #     my_cursor=con.cursor()
    #     my_cursor.execute("select * from  customer")
    #     rows= my_cursor.fetchall()
    #     for i in rows:
    #         self.cust_details_table.insert("",END,values=i)

    #     con.commit()
    #     con.close()

    # ==========///// Fetch Data /////////==========
    def fetch_data(self):
        # Connecting to the DATABASE
        con=cx_Oracle.connect('gautam/gautam123')
        # print(con.version)
        my_cursor=con.cursor()
        my_cursor.execute("select * from  customer")
        rows= my_cursor.fetchall()
        if len(rows)!=0:
            self.cust_details_table.delete(*self.cust_details_table.get_children())

            for i in rows:
                self.cust_details_table.insert("",END,values=i)

            con.commit()
        con.close()


    def get_cursor(self,events=""):
        cursor_row= self.cust_details_table.focus()
        content= self.cust_details_table.item(cursor_row)
        row= content["values"]


        self.ref.set(row[0])
        self.cname.set(row[1])
        self.fname.set(row[2])
        self.gender.set(row[3])
        self.postcode.set(row[4])
        self.mob.set(row[5])
        self.email.set(row[6])
        self.nationality.set(row[7])
        self.idproof.set(row[8])
        self.idnum.set(row[9])
        self.addrr.set(row[10])

    def update_btn(self):
        if self.ref.get()=="" or self.cname.get()=="" or self.fname.get()=="" or self.gender.get()=="" or self.postcode.get()=="" or self.mob.get()=="" or self.email.get()=="" or self.nationality.get()=="" or self.idproof.get()=="" or self.idnum.get()=="" or self.addrr.get()=="":
            messagebox.showerror("Form","All  Fields Are Required!!!!!",parent=self.root)
        else:
            r=self.ref.get()
            c=self.cname.get()
            f=self.fname.get()
            g=self.gender.get()
            p=self.postcode.get()
            m=self.mob.get()
            e=self.email.get()
            n=self.nationality.get()
            i=self.idproof.get()
            id=self.idnum.get()
            a=self.addrr.get()

        # Connecting to the DATABASE
            con=cx_Oracle.connect('gautam/gautam123')
            print(con.version)
            cursor=con.cursor()

            try:
                cursor.execute("UPDATE customer SET cname =:2,fname=:3,gender=:4,postcode=:5,mob=:6,email=:7,nationality=:8,idproof=:9,idnum=:10,addrr=:11 WHERE ref like '%s'"%r,(c,f,g,p,m,e,n,i,id,a))
                
                con.commit()
                self.fetch_data()  
                con.close()
            except cx_Oracle.IntegrityError:
                messagebox.showerror("ALREADY EXISTED","CUSTOMER ALREADY EXISTED IN THE LIST",parent=self.root)
            
            else:
                messagebox.showinfo("SUCCESS","RECORD UPDATED SUCCESFULLY",parent=self.root)

    def delete_btn(self):
        r=self.ref.get()
        if r=="":
            messagebox.showerror("Error","Ref number is Required to Delete the record!!",parent=self.root)
        else:
            con=cx_Oracle.connect("gautam/gautam123")
            cur=con.cursor()
            cur.execute("Delete From customer where ref = :id",id=r)
            #rows = cur.fetchall()
            con.commit()
            self.fetch_data()
            con.close()
            messagebox.showinfo("Success","Record Deleted Successfully",parent=self.root)
    
    def search_btn(self):
        con=cx_Oracle.connect("gautam/gautam123")
        cur=con.cursor()
        # cur.execute("select * from  customer where "+str(self.search_var.get())+"LIKE'%"+str(self.txt_search.get())+"%s'")
        rows= cur.fetchall()
        if len(rows)!= 0:
            self.cust_details_table.delete(* self.cust_details_table.get_children())

            for i in rows:
                self.cust_details_table.insert("",END,values=i)

            con.commit()
        # self.fetch_data()
        con.close()



            

            
if __name__=="__main__":
    root= Tk()
    obj= Cust_win(root)
    root.mainloop()