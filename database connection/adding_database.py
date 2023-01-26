from tkinter import * 
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
c.execute("""create table addresses(
    first_name varchar2(20),
    last_name varchar2(20),
    address varchar2(30),
    city varchar(20),
    state varchar2(20),
    zipcode number,
    sno number primary key
)
""")

# commit changes
conn.commit()

# close database connection
conn.close()






root.mainloop()
