from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox,ttk
import tkinter as tk
import pymysql

mydatabase="python_songs"
mypass = "abcd@1234"

def openview(view):
    root = Tk()
    root.title("View All Songs")
    root.minsize(width=40,height=4)
    root.geometry("1000x400")
    if(view=="Years"):
        tree = ttk.Treeview(root, column=("c1","c2"),show='headings')
        tree.column("#1", anchor=tk.CENTER)
        tree.heading("#1", text="Year")
        tree.column("#2", anchor=tk.CENTER)
        tree.heading("#2", text="Number of Tracks")
        tree.grid(sticky = (N,S,W,E))
        root.treeview = tree
        root.grid_rowconfigure(0, weight = 1)
        root.grid_columnconfigure(0, weight = 1)
        tree.pack(expand=True,fill=BOTH)
        try:
            con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
            cur = con.cursor()
            cur.execute("SELECT * FROM Tracks_by_Release_Year;")
            rows = cur.fetchall()
            con.commit()
            for i in rows:
                tree.insert("", tk.END, values=i)
        except:
            messagebox.showinfo('Error',"Failed To Fetch Songs From The Database")
    elif(view=="Languages"):
        tree = ttk.Treeview(root, column=("c1","c2"),show='headings')
        tree.column("#1", anchor=tk.CENTER)
        tree.heading("#1", text="Language")
        tree.column("#2", anchor=tk.CENTER)
        tree.heading("#2", text="Number of Albums")
        tree.grid(sticky = (N,S,W,E))
        root.treeview = tree
        root.grid_rowconfigure(0, weight = 1)
        root.grid_columnconfigure(0, weight = 1)
        tree.pack(expand=True,fill=BOTH)
        try:
            con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
            cur = con.cursor()
            cur.execute("SELECT * FROM Albums_in_Languages;")
            rows = cur.fetchall()
            con.commit()
            for i in rows:
                tree.insert("", tk.END, values=i)
        except:
            messagebox.showinfo('Error',"Failed To Fetch Songs From The Database")
    elif(view=="Genres"):
        tree = ttk.Treeview(root, column=("c1","c2"),show='headings')
        tree.column("#1", anchor=tk.CENTER)
        tree.heading("#1", text="Genre")
        tree.column("#2", anchor=tk.CENTER)
        tree.heading("#2", text="Number of Albums")
        tree.grid(sticky = (N,S,W,E))
        root.treeview = tree
        root.grid_rowconfigure(0, weight = 1)
        root.grid_columnconfigure(0, weight = 1)
        tree.pack(expand=True,fill=BOTH)
        try:
            con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
            cur = con.cursor()
            cur.execute("SELECT * FROM Albums_in_Genres;")
            rows = cur.fetchall()
            con.commit()
            for i in rows:
                tree.insert("", tk.END, values=i)
        except:
            messagebox.showinfo('Error',"Failed To Fetch Songs From The Database")
    else:
        messagebox.showinfo('Error',"Invalid View")


def diffviews(): 
    root = Toplevel()
    root.title("Views")
    root.minsize(width=1366,height=768)
    root.geometry("1366x768")
    mypass = "abcd@1234"
    mydatabase="python_songs"
    con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
    cur = con.cursor()
    background_image = Image.open("./images/count.jpg")
    background_image = ImageTk.PhotoImage(background_image)
    
    background_label = Label(root, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    root.minsize(width=1366,height=768)
    headingFrame1 = Frame(root, bg="black", bd=5)
    headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
        
    headingLabel = Label(headingFrame1, text="Views",font='Helvetica 14 bold', bg="white", fg='black',)
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    btn1 = Button(root,text="Number of track per release yeear",font='Helvetica 10 bold',bg='black', fg='white', command= lambda: openview("Years"))
    btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
    btn2 = Button(root,text="Albums by languages",font='Helvetica 10 bold',bg='black', fg='white', command= lambda: openview("Languages"))
    btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    
    btn3 = Button(root,text="Albums in genres",font='Helvetica 10 bold',bg='black', fg='white', command= lambda: openview("Genres"))
    btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
    
    root.mainloop()