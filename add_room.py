import email
import string
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



class Add_room_win:
    def __init__(self,root):
        self.root= root
        self.root.title("Hotel Management System")
        #widthx height + x + y
        self.root.geometry("1295x550+230+220")

        # variable to be used
        self.floor= StringVar()
        self.roomno= StringVar()
        self.roomtype= StringVar()


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
        labelframeleft = LabelFrame(self.root,relief=RIDGE,text="Adding New Room ",font="lucida 12 bold",bd=4,padx=2)
        labelframeleft.place(x=5,y=50,width=540,height=350)

        #====================labels and entry=============
        # room floor
        lbl_room_floor=Label (labelframeleft,text="Floor",font="lucida 12 bold",padx=2,pady=6)
        lbl_room_floor.grid(row=0,column=0)

        floor=ttk.Entry(labelframeleft,textvariable=self.floor,width=22,font="lucida 12 bold")
        floor.grid(row=0,column=1,sticky='w')

        # room number
        lbl_room_number=Label (labelframeleft,text="Room number",font="lucida 12 bold",padx=2,pady=6)
        lbl_room_number.grid(row=1,column=0)

        r_no=ttk.Entry(labelframeleft,textvariable=self.roomno,width=22,font="lucida 12 bold")
        r_no.grid(row=1,column=1,sticky='w')

        # Room type ///////////- luxury,deluxe,single ,double etc
        lbl_Room_type=Label (labelframeleft,text="Room Type",font="lucida 12 bold",padx=2,pady=6)
        lbl_Room_type.grid(row=2,column=0)

        r_type=ttk.Entry(labelframeleft,width=22,textvariable=self.roomtype,font="lucida 12 bold")
        r_type.grid(row=2,column=1,sticky='w')


        #=====================btn left frame==============
        btn_frame = Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add, font="lucida 12 bold",bg="black",fg="gold",width=9)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.update_btn,font="lucida 12 bold",bg="black",fg="gold",width=9)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.delete_btn,font="lucida 12 bold",bg="black",fg="gold",width=9)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.reset,font="lucida 12 bold",bg="black",fg="gold",width=9)
        btnReset.grid(row=0,column=3,padx=1)


        # ==================Label frame search system========================
        Table_frame = LabelFrame(self.root,relief=RIDGE,text="Details of all Room",font="lucida 12 bold",bd=4,padx=2)
        Table_frame.place(x=600,y=55,width=600,height=350)


        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.Table_frame= ttk.Treeview(Table_frame,columns=("floor","roomno","roomtype"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Table_frame.xview)
        scroll_y.config(command=self.Table_frame.yview)


        self.Table_frame.heading("floor",text="Floor")
        self.Table_frame.heading("roomno",text="Room no")
        self.Table_frame.heading("roomtype",text="Room type")
        
        self.Table_frame["show"]="headings"

        self.Table_frame.column("floor",width=100)
        self.Table_frame.column("roomno",width=100)
        self.Table_frame.column("roomtype",width=100)
        
        
        self.Table_frame.pack(fill=BOTH,expand=1)
        self.Table_frame.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    # add data into room
    def add(self):
        if self.roomno.get()=="" :
            messagebox.showerror("Error","pleae fill roomno and roomtype")

        else:
            f= self.floor.get()
            rno=self.roomno.get()
            rty=self.roomtype.get()
            

             # Connecting to the DATABASE
            con=cx_Oracle.connect('gautam/gautam123')
            # print(con.version)
            cursor=con.cursor()
            try:
                cursor.execute("INSERT INTO ADD_ROOM VALUES(:1,:2,:3)",(f,rno,rty))    
            except cx_Oracle.IntegrityError:
                messagebox.showerror("ALREADY EXISTED","ROOM ALREADY EXISTED",parent=self.root)
            
            else:
                con.commit()
                self.fetch_data()
                con.close()
                a=messagebox.showinfo("COMPLETED","ROOM ADDED SUCCESFULLY",parent=self.root)

    def reset(self):
        self.floor.set("")
        self.roomno.set("")
        self.roomtype.set("")

    # ==========///// Fetch Data /////////==========
    def fetch_data(self):
        # Connecting to the DATABASE
        con=cx_Oracle.connect('gautam/gautam123')
        # print(con.version)
        my_cursor=con.cursor()
        my_cursor.execute("select * from  add_room")
        rows= my_cursor.fetchall()
        if len(rows)!=0:
            self.Table_frame.delete(*self.Table_frame.get_children())

            for i in rows:
                self.Table_frame.insert("",END,values=i)

            con.commit()
        con.close()


     # ============== get cursor for updatation again /////////////////======
    def get_cursor(self,events=""):
        cursor_row= self.Table_frame.focus()
        content= self.Table_frame.item(cursor_row)
        row= content["values"]


        self.floor.set(row[0])
        self.roomno.set(row[1])
        self.roomtype.set(row[2])


    def update_btn(self):
        if self.roomno.get()==""  :
            messagebox.showerror("Form","please fill roomno and roomtype",parent=self.root)
        else:
            f= self.floor.get()
            rno= self.roomno.get()
            rty=self.roomtype.get()
            
        # Connecting to the DATABASE
            con=cx_Oracle.connect('gautam/gautam123')
            # print(con.version)
            cursor=con.cursor()

            try:
                cursor.execute("UPDATE ADD_ROOM SET FLOOR =:0,roomtype=:2 WHERE roomno like '%s'"%rno,(f,rty))
                
                con.commit()
                self.fetch_data()  
                con.close()
            except cx_Oracle.IntegrityError:
                messagebox.showerror("ALREADY EXISTED","ROOM ALREADY EXISTED IN THE LIST",parent=self.root)
            
            else:
                messagebox.showinfo("SUCCESS","RECORD UPDATED SUCCESFULLY",parent=self.root)


    # ===========/// Delete the records of room by ref number ///////===========
    def delete_btn(self):
        r=self.roomno.get()
        if r=="":
            messagebox.showerror("Error","Room number is Required to Delete the record!!",parent=self.root)
        else:
            con=cx_Oracle.connect("gautam/gautam123")
            cur=con.cursor()
            cur.execute("Delete From add_room where roomno = :id",id=r)
            #rows = cur.fetchall()
            con.commit()
            self.fetch_data()
            con.close()
            messagebox.showinfo("Success","Room Deleted Successfully",parent=self.root)

if __name__=="__main__":
    root= Tk()
    obj= Add_room_win(root)
    root.mainloop()
