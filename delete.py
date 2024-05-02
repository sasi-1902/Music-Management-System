from tkinter import *
from tkinter import messagebox

import pymysql
from PIL import ImageTk, Image
from tkinter import Toplevel
import tkinter as tk
from PIL import Image, ImageTk

mypass = "abcd@1234"
mydatabase = "python_songs"

con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
cur = con.cursor()


def deletesong():
    title = songInfo1.get()

    try:
        cur.execute("SELECT * FROM track WHERE title = %s;", (title,))
        if cur.fetchone():
            cur.execute("DELETE FROM track WHERE title = %s;", (title,))
            con.commit()
            messagebox.showinfo('Success', "Song Record Deleted Successfully")
        else:
            messagebox.showinfo("Song Not Found")
    except:
        messagebox.showinfo("Please Check Song Title")

    songInfo1.delete(0, END)
    root.destroy()

def delete():
    global img, songInfo1, songInfo2, songInfo3, songInfo4, songInfo5, Canvas1, con, cur, root

    root = tk.Toplevel()
    root.title("Delete Music Recordd")

    background_image = Image.open("./images/test1.jpeg")
    background_image = ImageTk.PhotoImage(background_image)

    background_label = Label(root, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    root.minsize(width=1366,height=768)
    headingFrame1 = Frame(root, bg="black", bd=5)
    headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)


    headingLabel = tk.Label(headingFrame1, text="Delete Song Record", font='Helvetica 14 bold', bg="#010103", fg='white')
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = tk.Frame(root, bg="#010103")
    labelFrame.place(relx=0.25, rely=0.3, relwidth=0.45, relheight=0.15)

    lb2 = tk.Label(labelFrame, text="Song Title:", font='Helvetica 11 bold', bg="#000000", fg='white')
    lb2.place(relx=0.05, rely=0)

    songInfo1 = tk.Entry(labelFrame)
    songInfo1.place(relx=0.3, rely=0, relwidth=0.62)

    SubmitBtn = tk.Button(root, text="Submit", font='Helvetica 11 bold', bg="#010103", fg='white', command=deletesong)
    SubmitBtn.place(relx=0.28, rely=.9, relwidth=0.18, relheight=0.08)

    quitBtn = tk.Button(root, text="Quit", font='Helvetica 11 bold', bg="#010103", fg='white', command=root.destroy)
    quitBtn.place(relx=0.53, rely=.9, relwidth=0.18, relheight=0.08)

    # def resize_image(event):
    #     img = Image.open("./images/delete.jpg")
    #     img = img.resize((event.width, event.height), Image.ANTIALIAS)
    #     img = ImageTk.PhotoImage(img)
    #     Canvas1.create_image(0, 0, image=img, anchor=NW)
    #     Canvas1.config(bg="black", width=event.width, height=event.height)

    # root.bind("<Configure>", resize_image)

    root.mainloop()