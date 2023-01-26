import re
from tkinter import *
from turtle import width
from unittest.main import main
from PIL import Image,ImageTk
from customer import Cust_win
from room import room
import cx_Oracle


class Cust_win:
    def __init__(self,root):
        self.root= root
        self.root.title("Hotel Management System")
        #widthx height + x + y
        self.root.geometry("1295x550+230+220")

        lbl_title= Label(self.root,text="ADD CUSTOMER DETAILS",font="lucida 18 bold",bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)






        labelframeleft = LabelFrame(self.root,relief=RIDGE,text="Customer Details",font="lucida 12 bold",bd=4,padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)


        # create text boxes
        f_name = Entry(labelframeleft,width=30)
        f_name.grid(row=0,column=1,padx=20,pady=(20,0))

        l_name = Entry(labelframeleft,width=30)
        l_name.grid(row=1,column=1,padx=20,pady=(20,0))

        address = Entry(labelframeleft,width=30)
        address.grid(row=2,column=1,padx=20,pady=(20,0))

        city = Entry(labelframeleft,width=30)
        city.grid(row=3,column=1,padx=20,pady=(20,0))

        state = Entry(labelframeleft,width=30)
        state.grid(row=4,column=1,padx=20,pady=(20,0))

        zipcode = Entry(labelframeleft,width=30)
        zipcode.grid(row=5,column=1,padx=20,pady=(20,0))

        sno = Entry(labelframeleft,width=30)
        sno.grid(row=6,column=1,padx=20,pady=(20,0))

        # create table labels

        f_name_label= Label(labelframeleft,text="First name")
        f_name_label.grid(row=0,column=0,pady=(20,0),padx=20)

        l_name_label= Label(labelframeleft,text="Last name")
        l_name_label.grid(row=1,column=0,pady=(20,0),padx=20)

        address_label= Label(labelframeleft,text="Address")
        address_label.grid(row=2,column=0,pady=(20,0),padx=20)

        city_label= Label(labelframeleft,text="City")
        city_label.grid(row=3,column=0,pady=(20,0),padx=20)

        state_label= Label(labelframeleft,text="State")
        state_label.grid(row=4,column=0,pady=(20,0),padx=20)

        zipcode_label= Label(labelframeleft,text="Zipcode")
        zipcode_label.grid(row=5,column=0,pady=(20,0),padx=20)

        sno_label= Label(labelframeleft,text="Sno")
        sno_label.grid(row=6,column=0,pady=(20,0),padx=20)

        # create submit button
        submit_btn= Button(labelframeleft,text = "Add record to database", command=self.submit)
        submit_btn.grid(row=8, column=0,columnspan=2,pady=10,padx=10,ipadx=100)


        query_btn= Button(labelframeleft,text = "Show all records" )
        query_btn.grid(row=9, column=0,columnspan=2,pady=10,padx=10,ipadx=100)


        # create submit function for database
    def submit(self):
    # create a database or connect to database:
        conn= cx_Oracle.connect("gautam/gautam123")

    # create cursor
        c = conn.cursor()

    # insert into table
        c.execute("insert into customer values(:f_name,:l_name,:address,:city,:state,:zipcode,:sno)",
    
        {
            'f_name': self.f_name.get(),
            'l_name': self.l_name.get(),
            'address':self.address.get(),
            'city': self.city.get(),
            'state': self.state.get(),
            'zipcode': self.zipcode.get(),
            'sno': self.sno.get()    
        })

# commit changes
        conn.commit()

# close database connection
        conn.close()




    # clear the text  boxes
        self.f_name.delete(0,END)
        self.l_name.delete(0,END)
        self.address.delete(0,END)
        self.city.delete(0,END)
        self.state.delete(0,END)
        self.zipcode.delete(0,END)
        self.sno.delete(0,END)



if __name__=="__main__":
    root= Tk()
    obj= Cust_win(root)
    root.mainloop()