from email.mime import image
from tkinter import *
from PIL import Image , ImageTk

root= Tk()
#root.geometry("1000x1200")

# for jpg images

imaget = Image.open("hotel\2.jpeg")
photo = ImageTk.PhotoImage(imaget)

lab1= Label(image= photo)
lab1.pack()



root.mainloop()