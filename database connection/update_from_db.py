from tkinter import *
from turtle import width
from wsgiref import validate 
from PIL import ImageTk,Image
import cx_Oracle

root= Tk()
root.geometry("400x600")
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

def edit():
    # create a database or connect to database:
    conn= cx_Oracle.connect("scott/tiger")

    # create cursor
    c = conn.cursor()  


    record_id =delete_box.get()
    # write query to execute update/edit statement
    c.execute(""" update addresses set
            f_name =:first,
            l_name= :last,
            address = :address,
            city = :city,
            state= :state,
            zipcode = :zipcode""",
            
            f_name= f_name_editor.get(),
            l_name= l_name_editor.get(),
            address= address_editor.get(),
            city= city_editor.get(),
            state =state_editor.get(),
            zipcode= zipcode_editor.get(),
            sno= sno_editor.get() 
            )

    # commit changes
    conn.commit()

    # close database connection
    conn.close()

    


# create update function 
def update():
    editor= Tk()
    editor.geometry("400x600")
    editor.title("update or edit your text")

    # create a database or connect to database:
    conn= cx_Oracle.connect("scott/tiger")

    # create cursor
    c = conn.cursor()
    
    record_id = delete_box.get()
    # Query of the database to show records
    c.execute("select * from addresses where sno="+record_id)
    records=c.fetchall()

    # create a Global variable of all entry box so we use in this another window;
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor
    global sno_editor

    # create text boxes
    f_name_editor = Entry(editor,width=30)
    f_name_editor.grid(row=0,column=1,padx=20,pady=(20,0))

    l_name_editor = Entry(editor,width=30)
    l_name_editor.grid(row=1,column=1,padx=20,pady=(20,0))

    address_editor = Entry(editor,width=30)
    address_editor.grid(row=2,column=1,padx=20,pady=(20,0))

    city_editor = Entry(editor,width=30)
    city_editor.grid(row=3,column=1,padx=20,pady=(20,0))

    state_editor = Entry(editor,width=30)
    state_editor.grid(row=4,column=1,padx=20,pady=(20,0))

    zipcode_editor = Entry(editor,width=30)
    zipcode_editor.grid(row=5,column=1,padx=20,pady=(20,0))

    sno_editor = Entry(editor,width=30)
    sno_editor.grid(row=6,column=1,padx=20,pady=(20,0))

    # create form labels

    f_name_label= Label(editor,text="First name")
    f_name_label.grid(row=0,column=0,pady=(20,0),padx=20)

    l_name_label= Label(editor,text="Last name")
    l_name_label.grid(row=1,column=0,pady=(20,0),padx=20)

    address_label= Label(editor,text="Address")
    address_label.grid(row=2,column=0,pady=(20,0),padx=20)

    city_label= Label(editor,text="City")
    city_label.grid(row=3,column=0,pady=(20,0),padx=20)

    state_label= Label(editor,text="State")
    state_label.grid(row=4,column=0,pady=(20,0),padx=20)

    zipcode_label= Label(editor,text="Zipcode")
    zipcode_label.grid(row=5,column=0,pady=(20,0),padx=20)

    sno_label= Label(editor,text="Sno")
    sno_label.grid(row=6,column=0,pady=(20,0),padx=20)

    # Loop through results
    for record in records:
        f_name_editor.insert(0,record[0])
        l_name_editor.insert(0,record[1])
        address_editor.insert(0,record[2])
        city_editor.insert(0,record[3])
        state_editor.insert(0,record[4])
        zipcode_editor.insert(0,record[5])
        sno_editor.insert(0,record[6])
    

    #create a save  button to save updated data
    edit_btn= Button(editor,text = "Save Record", command=edit )
    edit_btn.grid(row=8, column=0,columnspan=2,pady=10,padx=10,ipadx=100)




# create delete function for database
def delete():
    # create a database or connect to database:
    conn= cx_Oracle.connect("scott/tiger")

    # create cursor
    c = conn.cursor()

    # delete a record
    c.execute("delete from addresses where sno="+delete_box.get())

    # commit changes
    conn.commit()

    # close database connection
    conn.close()


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
    # then we take records is a variable that store value of all fetched
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
    query_label.grid(row=14,column=0,columnspan=2)



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

delete_box = Entry(root,width=30)
delete_box.grid(row=10,column=1,padx=20,pady=(20,0))

delete_label= Label(root,text="Select sno")
delete_label.grid(row=10,column=0,pady=(20,0),padx=20)



# create form labels

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

# query button
query_btn= Button(root,text = "Show all records", command=query )
query_btn.grid(row=9, column=0,columnspan=2,pady=10,padx=10,ipadx=100)

# delete button
delete_btn= Button(root,text = "Delete Record", command=delete )
delete_btn.grid(row=11, column=0,columnspan=2,pady=10,padx=10,ipadx=100)

#update button
edit_btn= Button(root,text = "Edit Record", command=update )
edit_btn.grid(row=12, column=0,columnspan=2,pady=10,padx=10,ipadx=100)



# commit changes
conn.commit()

# close database connection
conn.close()

root.mainloop()
