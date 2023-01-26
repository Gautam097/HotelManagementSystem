from tkinter import *
from turtle import width 
from PIL import ImageTk,Image
import cx_Oracle

root= Tk()
root.geometry("400x400")
root.title("Database connection")

# Database

# create a database or connect to database:
conn= cx_Oracle.connect("scott/tiger")

# create cursor
c = conn.cursor()




# create table

# c.execute("""create table addresses(
#     first_name varchar2(20),
#     last_name varchar2(20),
#     address varchar2(30),
#     city varchar(20),
#     state varchar2(20),
#     zipcode number,
#     sno number primary key
# )
# """)

# create submit function for database
def submit():
    # create a database or connect to database:
    conn= cx_Oracle.connect("scott/tiger")

    # create cursor
    c = conn.cursor()

    # insert into table
    c.execute("insert into addresses values(:f_name,:l_name,:address,:city,:state,:zipcode,:sno)",
    
        {
            'f_name': f_name.get(),
            'l_name': l_name.get(),
            'address': address.get(),
            'city': city.get(),
            'state': state.get(),
            'zipcode': zipcode.get(),
            'sno': sno.get()    
        })

# commit changes
    conn.commit()

# close database connection
    conn.close()




    # clear the text  boxes
    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    zipcode.delete(0,END)
    sno.delete(0,END)


# create query function
def query():
    # create a database or connect to database:
    conn= cx_Oracle.connect("scott/tiger")

# create cursor
    c = conn.cursor()

# Query of the database to show records

    c.execute("select * from addresses")
    # c.fetchone()
    # c.fetchmany(50)
    records=c.fetchall()
    # print(c.fetchall)
    #print(records)


    # loop through results ( first methods to show )
    # print_records=""
    # for record in records:
    #     print_records += str(record) + "\n"

    print_records=""
    for record in records:
        print_records += str(record[0]) + "  " + str(record[1]) + " "+ " \t "+ str(record[6])  +"\n"


    query_label = Label(root, text=print_records)
    query_label.grid(row=10,column=0,columnspan=2)



# commit changes
    conn.commit()

# close database connection
    conn.close()



# create text boxes
f_name = Entry(root,width=30)
f_name.grid(row=0,column=1,padx=20,pady=(20,0))

l_name = Entry(root,width=30)
l_name.grid(row=1,column=1,padx=20,pady=(20,0))

address = Entry(root,width=30)
address.grid(row=2,column=1,padx=20,pady=(20,0))

city = Entry(root,width=30)
city.grid(row=3,column=1,padx=20,pady=(20,0))

state = Entry(root,width=30)
state.grid(row=4,column=1,padx=20,pady=(20,0))

zipcode = Entry(root,width=30)
zipcode.grid(row=5,column=1,padx=20,pady=(20,0))

sno = Entry(root,width=30)
sno.grid(row=6,column=1,padx=20,pady=(20,0))

# create table labels

f_name_label= Label(root,text="First name")
f_name_label.grid(row=0,column=0,pady=(20,0),padx=20)

l_name_label= Label(root,text="Last name")
l_name_label.grid(row=1,column=0,pady=(20,0),padx=20)

address_label= Label(root,text="Address")
address_label.grid(row=2,column=0,pady=(20,0),padx=20)

city_label= Label(root,text="City")
city_label.grid(row=3,column=0,pady=(20,0),padx=20)

state_label= Label(root,text="State")
state_label.grid(row=4,column=0,pady=(20,0),padx=20)

zipcode_label= Label(root,text="Zipcode")
zipcode_label.grid(row=5,column=0,pady=(20,0),padx=20)

sno_label= Label(root,text="Sno")
sno_label.grid(row=6,column=0,pady=(20,0),padx=20)

# create submit button
submit_btn= Button(root,text = "Add record to database", command=submit)
submit_btn.grid(row=8, column=0,columnspan=2,pady=10,padx=10,ipadx=100)


query_btn= Button(root,text = "Show all records", command=query )
query_btn.grid(row=9, column=0,columnspan=2,pady=10,padx=10,ipadx=100)



# commit changes
conn.commit()

# close database connection
conn.close()






root.mainloop()
