from tkinter import *
from PIL import Image, ImageTk
import pymysql
from tkinter import messagebox
from tkinter.ttk import *
from add import *
from delete import *
from Explore import *

mypass = "abcd@1234"
mydatabase="python_songs"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

root = Tk()
root.title("Music Library Management System")

background_image = Image.open("./images/main.jpg")
background_image = ImageTk.PhotoImage(background_image)

background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
root.minsize(width=1366,height=768)
headingFrame1 = Frame(root, bg="black", bd=5)
headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

headingLabel = Label(headingFrame1, text="Welcome to\nMusic Library Management System", bg="black", fg='white', font=('Courier',15))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

btn1 = Button(root, text="Add Track", font='Helvetica 10 bold', bg='white', fg='black', command=addsong)
btn1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

btn2 = Button(root, text="Delete Track", font='Helvetica 10 bold', bg='white', fg='black', command=delete)
btn2.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

btn3 = Button(root, text="Explore Tracks", font='Helvetica 10 bold', bg='white', fg='black', command=view)
btn3.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

# root.resizable(True, True)  
root.mainloop()