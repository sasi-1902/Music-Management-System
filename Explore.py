from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

from viewallsongs import *
from viewgenere import *
from viewlanguages import *
from numbersview import*

mypass = "abcd@1234"
mydatabase="python_songs"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()
    
def view(): 
    
    root = Toplevel()
    root.title("Explore Tracks")
    root.minsize(width=400, height=400)
    root.geometry("1366x768")

    background_image = Image.open("./images/view.jpg")
    [imageSizeWidth, imageSizeHeight] = background_image.size
    newImageSizeWidth = int(imageSizeWidth * 0.8)
    newImageSizeHeight = int(imageSizeHeight * 0.8)
    background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight), Image.BILINEAR)
    img = ImageTk.PhotoImage(background_image)

    Canvas1 = Canvas(root)
    Canvas1.create_image(300, 340, image=img)
    Canvas1.config(bg="black", width=newImageSizeWidth, height=newImageSizeHeight)
    Canvas1.pack(expand=True, fill=BOTH)
            
    headingFrame1 = Frame(root,bg="white",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Explore Songs",font='Helvetica 14 bold', bg="#090a0c", fg='white', )
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    btn1 = Button(root,text="All Songs",font='Helvetica 10 bold',bg='black', fg='white', command=viewallsongs)
    btn1.place(relx=0.28,rely=0.42, relwidth=0.45,relheight=0.1)

    btn2 = Button(root,text="View Genres",font='Helvetica 10 bold',bg='black', fg='white', command=viewgenre)
    btn2.place(relx=0.28,rely=0.52, relwidth=0.45,relheight=0.1)
    
    btn3 = Button(root,text="Checkout Languages",font='Helvetica 10 bold',bg='black', fg='white', command=viewlanguage)
    btn3.place(relx=0.28,rely=0.62, relwidth=0.45,relheight=0.1)
    
    btn4 = Button(root,text="Different Views",font='Helvetica 10 bold',bg='black', fg='white', command=diffviews)
    btn4.place(relx=0.28,rely=0.72, relwidth=0.45,relheight=0.1)

    root.mainloop()
