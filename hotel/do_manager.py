from cProfile import label
from email import message
from email.mime import image
from platform import release
from struct import pack
from sys import maxsize
from tkinter import *
from tkinter import messagebox
from turtle import bgcolor, dot, title, up, width
import tkinter.font as TkFont
from tkinter import ttk
from webbrowser import BackgroundBrowser
import cx_Oracle
from PIL import Image,ImageTk

class manage():
    def _init_(self,winmanager):
        self.winmanager=winmanager
        self.winmanager.title('Manager page')
        self.winmanager.geometry('1600x1204+0+0')
        # self.winmanager.minsize(1255,944)
        # self.winmanager.maxsize(1255,944)
        l1=Label(self.winmanager,text="welvome")
        l1.pack()

        # Variables to use
        self.movieid_var=StringVar()
        self.moviename_var=StringVar()
        self.movietype_var=StringVar()
        self.movierdate=StringVar()
        self.movieactor_var=StringVar()
        self.movieactress_var=StringVar()
        self.moviedirector_var=StringVar()
        self.movielength_var=StringVar()
        self.movieseats_var=StringVar()
        self.movietheatre_var=StringVar()
        
        self.login_image=ImageTk.PhotoImage(Image.open('2.jpg'))
        login_label=Label(self.winmanager,image=self.login_image)
        login_label.place(x=0,y=0,relwidth=1,relheight=1)

        title_frame=Frame(self.winmanager)
        title_frame.pack()
        registration_text=Label(title_frame,text='Movie/..../Managing',font=("magneto",30,"bold"),bd=5,borderwidth=13,bg='#7d1515',relief=RAISED)
        # registration_text.place(x=20,y=0,relx=1,rely=1)
        registration_text.pack()


         #LeftSideFrame//////////////////////////////////////////////////////////////////      
        f1=Frame(self.winmanager,bd=4,relief=RAISED,borderwidth=7,bg='#5e6269')
        f1.place(x=30,y=135,width=420,height=640)

        f1.columnconfigure(0,weight=3)
        f1.columnconfigure(1,weight=3)

        movie_id=Label(f1,text='MOVIE ID :-',font=("magneto",12,"bold"),bd=5,relief=RAISED,bg='#6f747d',width=15)
        movie_id.grid(row=0,column=0,padx=0,pady=14)

        movie_id_entry=Entry(f1,textvariable=self.movieid_var,width=30,relief=SUNKEN,bg='#7d1515',bd=5,fg='white',font=("times",10,"bold"))
        movie_id_entry.grid(row=0,column=1,padx=5,pady=5)

        movie_name=Label(f1,text='NAME :-',font=("magneto",12,"bold"),bd=5,relief=RAISED,bg='#6f747d',width=15)
        movie_name.grid(row=1,column=0,padx=0,pady=8)

        movie_name_entry=Entry(f1,textvariable=self.moviename_var,width=30,relief=SUNKEN,bg='#7d1515',bd=5,fg='white',font=("times",10,"bold"))
        movie_name_entry.grid(row=1,column=1,padx=5,pady=5)

        movie_type=Label(f1,text='TYPE :-',font=("magneto",12,"bold"),bd=5,relief=RAISED,bg='#6f747d',width=15)
        movie_type.grid(row=2,column=0,pady=8)
        
        movie_type_entry=Entry(f1,textvariable=self.movietype_var,width=30,relief=SUNKEN,bg='#7d1515',bd=5,fg='white',font=("times",10,"bold"))
        # movie_type_entry.insert(0,'male or female')
        movie_type_entry.grid(row=2,column=1,padx=5,pady=5)
        
        release_date=Label(f1,text='RELEASE DATE :-',font=("magneto",12,"bold"),bd=5,relief=RAISED,bg='#6f747d',width=15)
        release_date.grid(row=3,column=0,pady=8)

        release_date_entry=Entry(f1,textvariable=self.movierdate,width=30,relief=SUNKEN,bg='#7d1515',bd=5,fg='white',font=("times",10,"bold"))
        release_date_entry.grid(row=3,column=1,padx=5,pady=5)

        movie_actor=Label(f1,text='ACTOR :-',font=("magneto",12,"bold"),bd=5,relief=RAISED,bg='#6f747d',width=15)
        movie_actor.grid(row=4,column=0,pady=8)

        movie_actor_entry=Entry(f1,textvariable= self.movieactor_var,width=30,relief=SUNKEN,bg='#7d1515',bd=5,fg='white',font=("times",10,"bold"))
        movie_actor_entry.grid(row=4,column=1,padx=5,pady=5)

        movie_actoress=Label(f1,text='ACTORESS :-',font=("magneto",12,"bold"),bd=5,relief=RAISED,bg='#6f747d',width=15)
        movie_actoress.grid(row=5,column=0,pady=8)
 
        movie_actoress_entry=Entry(f1,textvariable= self.movieactress_var,width=30,relief=SUNKEN,bg='#7d1515',bd=5,fg='white',font=("times",10,"bold"))
        movie_actoress_entry.grid(row=5,column=1,padx=5,pady=5)
        
        movie_director=Label(f1,text='DIRECTOR :-',font=("magneto",12,"bold"),bd=5,relief=RAISED,bg='#6f747d',width=15)
        movie_director.grid(row=6,column=0,pady=8)
 
        movie_director_entry=Entry(f1,textvariable=self.moviedirector_var,width=30,relief=SUNKEN,bg='#7d1515',bd=5,fg='white',font=("times",10,"bold"))
        movie_director_entry.grid(row=6,column=1,padx=5,pady=5)

        movie_length=Label(f1,text='LENGTH :-',font=("magneto",12,"bold"),bd=5,relief=RAISED,bg='#6f747d',width=15)
        movie_length.grid(row=7,column=0,pady=8)
 
        movie_length_entry=Entry(f1,textvariable=self.movielength_var,width=30,relief=SUNKEN,bg='#7d1515',bd=5,fg='white',font=("times",10,"bold"))
        movie_length_entry.grid(row=7,column=1,padx=5,pady=5)

        movie_seats=Label(f1,text='SEATS :-',font=("magneto",12,"bold"),bd=5,relief=RAISED,bg='#6f747d',width=15)
        movie_seats.grid(row=8,column=0,pady=8)
 
        movie_seats_entry=Entry(f1,textvariable=self.movieseats_var,width=30,relief=SUNKEN,bg='#7d1515',bd=5,fg='white',font=("times",10,"bold"))
        movie_seats_entry.grid(row=8,column=1,padx=5,pady=5)
        
        movie_theatre=Label(f1,text='THEATRE :-',font=("magneto",12,"bold"),bd=5,relief=RAISED,bg='#6f747d',width=15)
        movie_theatre.grid(row=9,column=0,pady=8)
 
        movie_theatre_entry=Entry(f1,textvariable=self.movietheatre_var,width=30,relief=SUNKEN,bg='#7d1515',bd=5,fg='white',font=("times",10,"bold"))
        movie_theatre_entry.grid(row=9,column=1,padx=5,pady=5)
        

        insert_button=Button(f1,text='INSERT',bd=6,borderwidth=6,bg='#ad1a1a',width=15,font=("magneto",12,"bold"),command=self.add_data)
        insert_button.grid(row=10,column=0,padx=5,pady=10)

        update_button=Button(f1,text='UPDATE',bd=6,borderwidth=6,bg='#ad1a1a',width=15,font=("magneto",12,"bold"),command=self.update_data)
        update_button.grid(row=10,column=1,padx=5,pady=20)

        delete_button=Button(f1,text='DELETE',bd=6,borderwidth=6,bg='#ad1a1a',width=15,font=("magneto",12,"bold"),command=self.delete_data)
        delete_button.grid(row=11,column=0,padx=5,pady=5)

        clear_button=Button(f1,text='CLEAR',bd=6,borderwidth=6,bg='#ad1a1a',width=15,font=("magneto",12,"bold"),command=self.clear_data)
        clear_button.grid(row=11,column=1,padx=5,pady=5)

        quit_buttom=Button(self.winmanager,text="QUIT AND GO BACK",bd=7,borderwidth=9,bg='#ad1a1a',width=22,font=("magneto",14,"bold"),command=self.quit)
        quit_buttom.place(x=880,y=720)


        #TreeviewFrame///////////////////////////////////////////////////////////////////
        f2=Frame(self.winmanager,bd=4,borderwidth=12,relief=RIDGE,bg='#5e6269')
        f2.place(x=590,y=136,width=900,height=560)   
        scroll_x=Scrollbar(f2,orient=HORIZONTAL)
        scroll_y=Scrollbar(f2,orient=VERTICAL)

        self.Movie_Table=ttk.Treeview(f2,columns=("ID","NAME","TYPE","RELEASE DATE","HEROES","HEROINES","DIRECTOR","LENGTH","SEATS","THEATRE"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Movie_Table.xview)
        scroll_y.config(command=self.Movie_Table.yview)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", font=("times new roman",15,"bold"),fieldbackground='#ad1a1a',background='#ad1a1a')
        style.configure("Treeview",background='#5e6269',fieldbackground='#5e6269',fieldforground="white",forground="white")
        # style.theme_use("vista")

        self.Movie_Table.heading("ID",text="ID")
        self.Movie_Table.heading("NAME",text="NAME")
        self.Movie_Table.heading("TYPE",text="TYPE")
        self.Movie_Table.heading("RELEASE DATE",text="RELEASE DATE")
        self.Movie_Table.heading("HEROES",text="HEROES")
        self.Movie_Table.heading("HEROINES",text="HEROINES")
        self.Movie_Table.heading("DIRECTOR",text="DIRECTOR")
        self.Movie_Table.heading("LENGTH",text="LENGTH")
        self.Movie_Table.heading("SEATS",text="SEATS")
        self.Movie_Table.heading("THEATRE",text="THEATRE")
        self.Movie_Table['show']="headings"
        self.Movie_Table.column("ID",width=80)
        self.Movie_Table.column("NAME",width=150)
        self.Movie_Table.column("TYPE",width=120)
        self.Movie_Table.column("RELEASE DATE",width=120)
        self.Movie_Table.column("HEROES",width=180)
        self.Movie_Table.column("HEROINES",width=180)
        self.Movie_Table.column("DIRECTOR",width=150)
        self.Movie_Table.column("LENGTH",width=80)
        self.Movie_Table.column("SEATS",width=80)
        self.Movie_Table.column("THEATRE",width=80)
        self.Movie_Table.bind("<ButtonRelease-1>",self.get_data)

        self.Movie_Table.pack(fill=BOTH,expand=1)
        self.fetch_data()
        
# Class Methods///////////////////////////////////////////////////////////////////////////////


    def add_data(self):
        if self.movieid_var.get()=="" or self.moviename_var.get()==""or self.movietype_var.get()==""or self.movierdate.get()==""or self.movieactor_var.get()=="" or self.movieactress_var.get()=="" or self.moviedirector_var.get()=="" or self.movielength_var.get()=="" or self.movieseats_var.get()=="" or self.movietheatre_var.get()=="":
             messagebox.showerror("Error","All (*) Fields Are Required!!!",parent=self.winmanager)
        else:
            I=self.movieid_var.get()
            N=self.moviename_var.get()
            TY=self.movietype_var.get()
            DA=self.movierdate.get()
            AT=self.movieactor_var.get()
            AR=self.movieactress_var.get()
            DI=self.moviedirector_var.get()
            L=self.movielength_var.get()
            S=eval(self.movieseats_var.get())
            TH=self.movietheatre_var.get()
             # Connecting to the DATABASE
            con=cx_Oracle.connect('cinema/danish30')
            print(con.version)
            cursor=con.cursor()
            try:
                cursor.execute("INSERT INTO movie_details VALUES(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10)",(I,N,TY,DA,AT,AR,DI,L,S,TH))    
            except cx_Oracle.IntegrityError:
                messagebox.showerror("ALREADY EXISTED","MOVIE ALREADY EXISTED")
            
            else:
                con.commit()
                self.fetch_data()
                con.close()
                a=messagebox.showinfo("COMPLETED","MOVIE ADDED SUCCESFULLY")
                # if (a=='ok'):
                #     b=messagebox.askyesno("PERMISSION","GO BACK TO THE LOGIN PAGE")
                #     if(b=='yes'):
                #         self.winmanager.quit()

                        
    def get_data(self,event):
        cursor_row=self.Movie_Table.focus()
        contents=self.Movie_Table.item(cursor_row)
        row=contents['values']
        self.movieid_var.set(row[0])
        self.moviename_var.set(row[1])
        self.movietype_var.set(row[2])
        self.movierdate.set(row[3])
        self.movieactor_var.set(row[4])
        self.movieactress_var.set(row[5])
        self.moviedirector_var.set(row[6])
        self.movielength_var.set(row[7])
        self.movieseats_var.set(row[8])
        self.movietheatre_var.set(row[9])
        
        

    def fetch_data(self):
        con=cx_Oracle.connect("cinema/danish30")
        cur=con.cursor()
        cur.execute("select * from Movie_Details")
        rows = cur.fetchall()
        if (rows)!=0:
            self.Movie_Table.delete(*self.Movie_Table.get_children())
            for row in rows:
                self.Movie_Table.insert('',END,values=row)
            con.commit()
        con.close()

    def update_data(self):
        if self.movieid_var.get()=="" or self.moviename_var.get()==""or self.movietype_var.get()==""or self.movierdate.get()==""or self.movieactor_var.get()=="" or self.movieactress_var.get()=="" or self.moviedirector_var.get()=="" or self.movielength_var.get()=="" or self.movieseats_var.get()=="" or self.movietheatre_var.get()=="":
             messagebox.showerror("Error","All (*) Fields Are Required!!!",parent=self.winmanager)
        
        else:
            I=self.movieid_var.get()
            N=self.moviename_var.get()
            TY=self.movietype_var.get()
            DA=self.movierdate.get()
            AT=self.movieactor_var.get()
            AR=self.movieactress_var.get()
            DI=self.moviedirector_var.get()
            L=self.movielength_var.get()
            S=eval(self.movieseats_var.get())
            TH=self.movietheatre_var.get()
             # Connecting to the DATABASE
            con=cx_Oracle.connect('cinema/danish30')
            print(con.version)
            cursor=con.cursor()
            try:
                cursor.execute("UPDATE MOVIE_DETAILS SET MOVIE_NAME= :1,MOVIE_TYPE= :2,RELEASE_DATE= :3,ACTOR= :4,ACTORESS= :5,DIRECTOR= :6,LENGTH= :7 ,SEATS= :8,THEATRE= :9 WHERE MOVIE_ID LIKE '%s'"%I,(N,TY,DA,AT,AR,DI,L,S,TH))
                # sql="UPDATE MOVIE_DETAILS SET MOVIE_NAME=:2,MOVIE_TYPE=:3,RELEASE_DATE=:4,ACTOR=:5,ACTORESS=:6,DIRECTOR=:7,LENGTH=:8 ,SEATS=:9,THEATRE=:10,where MOVIE_ID=:1"
                # cursor.execute (sql,(N,TY,DA,AT,AR,DI,L,S,TH,I))
                con.commit()
                self.fetch_data()  
                con.close()
            except cx_Oracle.IntegrityError:
                messagebox.showerror("ALREADY EXISTED","MOVIE ALREADY EXISTED IN THE LIST")
            
            else:
                
                
                messagebox.showinfo("SUCCESS","RECORD UPDATED SUCCESFULLY")
                # if (a=='ok'):
                #     b=messagebox.askyesno("PERMISSION","GO BACK TO THE LOGIN PAGE")
                #     if(b=='yes'):
                #         self.winmanager.quit()
     

    def delete_data(self):
        I=self.movieid_var.get()
        if I=="":
            messagebox.showerror("Error","Movie ID is Required to Delete the record!!",parent=self.winmanager)
        else:
            con=cx_Oracle.connect("cinema/danish30")
            cur=con.cursor()
            cur.execute("Delete From Movie_Details where MOVIE_ID = :id",id=I)
            #rows = cur.fetchall()
            con.commit()
            self.fetch_data()
            con.close()
            messagebox.showinfo("Success","Record Deleted Successfully",parent=self.winmanager)
    
    def clear_data(self):


        # if self.movieid_var.get()=="" or self.moviename_var.get()==""or self.movietype_var.get()==""or self.movierdate.get()==""or self.movieactor_var.get()=="" or self.movieactress_var.get()=="" or self.moviedirector_var.get()=="" or self.movielength_var.get()=="" or self.movieseats_var.get()=="" or self.movietheatre_var.get()=="":

        #     messagebox.showerror("Error","All (*) Fields Are Required!!!",parent=self.winmanager)
        
        
        self.movieid_var.set('')
        self.moviename_var.set('')
        self.movietype_var.set('')
        self.movierdate.set('')
        self.movieactor_var.set('')
        self.movieactress_var.set('')
        self.moviedirector_var.set('')
        self.movielength_var.set('')
        self.movieseats_var.set('')
        self.movietheatre_var.set('')    
        # messagebox.showinfo("Success","Fields Cleared Successfully",parent =self.winmanager)

    def quit(self):
        print()
        self.winmanager.destroy()   






# root0=Toplevel()
# ob=manage(root0)
# root0.mainloop()


if __name__ =="main":    
   winmanager=Tk()
   ob=manage(winmanager)
   winmanager.mainloop()