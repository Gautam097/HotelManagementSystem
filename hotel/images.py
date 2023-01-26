from tkinter import *
root= Tk()
root.geometry("1255x944")
#photo= PhotoImage(file="C:\Users\HP\OneDrive\Desktop\HMS using tkinter\hotel\8.png")
photo= PhotoImage(file="hotel\8.png")


lable1= Label(image=photo)
lable1.place(x=0,y=0,relheight=1,relwidth=1)


root.mainloop()
