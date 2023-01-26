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
from customer import Cust_win
import cx_Oracle


class showdetails:
    def __init__(self,root):
        self.root= root
        self.root.title("For Show Details")
        self.root.geometry("1295x550+230+220")


        # ==================== Title image ============
        lbl_title= Label(self.root,text="ADD ROOM IN HOTEL",font="lucida 18 bold",bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)


        # =================== logo image =============
        img2= Image.open("112.jpg")
        img2=img2.resize((100,40))
        self.photoimg2= ImageTk.PhotoImage(img2)

        lblimg = Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=3,width=100,height=40)

        # =====================Label frame =================
        labelframeleft = LabelFrame(self.root,relief=RIDGE,text="check all details of guest ",font="lucida 12 bold",bd=4,padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)

        lbl_of_ref=Label (labelframeleft,text="References number",font="lucida 12 bold",padx=2,pady=6)
        lbl_of_ref.grid(row=0,column=0)

        self.ref = StringVar()
        ref_entry=ttk.Entry(labelframeleft,textvariable=self.ref,width=22,font="lucida 12 bold")
        ref_entry.grid(row=0,column=1,sticky='w')

        lbl_of_retrive=Label (labelframeleft,text="Retrive all data",font="lucida 12 bold",padx=2,pady=6)
        lbl_of_retrive.grid(row=1,column=0)


        btnReset=Button(labelframeleft,text="Retrive All",command=self.fetch_data,font="lucida 12 bold",bg="black",fg="gold",width=9)
        btnReset.grid(row=1,column=1,padx=1)







        # ==================Label frame search system========================
        Table_frame = LabelFrame(self.root,relief=RIDGE,text="Details of all Guest",font="lucida 12 bold",bd=4,padx=2)
        Table_frame.place(x=435,y=50,width=860,height=490)

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
        self.fetch_data()





    def fetch_data(self):
        d = self.ref.get()
        # if d=="":
        #     messagebox.showerror("Error","please enter reference number",parent=self.root)

        # else:
        
        # Connecting to the DATABASE
        con=cx_Oracle.connect('gautam/gautam123')
        # print(con.version)
        my_cursor=con.cursor()
        my_cursor.execute("select * from  customer where ref= :ref",ref= d)
        rows= my_cursor.fetchall()
        if len(rows)!=0:
            self.cust_details_table.delete(*self.cust_details_table.get_children())
            for i in rows:
                self.cust_details_table.insert("",END,values=i)
            con.commit()
        con.close()

















if __name__=="__main__":
    root= Tk()
    obj= showdetails(root)
    root.mainloop()
