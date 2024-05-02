from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox,ttk
import tkinter as tk
import pymysql

mypass = "abcd@1234"
mydatabase="python_songs"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()
    
def viewlang(lang): 
    
    root = Tk()
    root.title("View "+lang.capitalize()+" Songs")
    root.minsize(width=400,height=400)
    root.geometry("1000x400")
    
    tree = ttk.Treeview(root, column=("c1","c2","c3","c4","c5",),show='headings')
    tree.column("#1", anchor=tk.CENTER)
    tree.heading("#1", text="Title")
    tree.column("#2", anchor=tk.CENTER)
    tree.heading("#2", text="Artist")
    tree.column("#3", anchor=tk.CENTER)
    tree.heading("#3", text="Album")
    tree.column("#4", anchor=tk.CENTER)
    tree.heading("#4", text="Genre")
    tree.column("#5", anchor=tk.CENTER)
    tree.heading("#5", text="Release Year")
    tree.grid(sticky = (N,S,W,E))
    root.treeview = tree
    root.grid_rowconfigure(0, weight = 1)
    root.grid_columnconfigure(0, weight = 1)
    tree.pack(expand=True,fill=BOTH)
    
    try:
        cur.execute("SELECT t.title, a.artist_name, al.album_name, l.language_name, t.rlsyr FROM track t JOIN album al ON t.album_id=al.id JOIN artist a ON t.artist_id=a.id JOIN genre g ON t.genre_id=g.id JOIN language l ON t.language_id=l.id WHERE l.language_name='"+lang+"';")
        rows = cur.fetchall()
        con.commit()
        
        for i in rows:
            tree.insert("", tk.END, values=i)
        
    except:
        messagebox.showinfo('Error',"Failed To Fetch Songs From The Database")

    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
    
    
def otherlang(): 
    
    root = Tk()
    root.title("Other Songs")
    root.minsize(width=400,height=400)
    root.geometry("1000x400")
    
    tree = ttk.Treeview(root, column=("c1","c2","c3","c4","c5",),show='headings')
    tree.column("#1", anchor=tk.CENTER)
    tree.heading("#1", text="Title")
    tree.column("#2", anchor=tk.CENTER)
    tree.heading("#2", text="Artist")
    tree.column("#3", anchor=tk.CENTER)
    tree.heading("#3", text="Album")
    tree.column("#4", anchor=tk.CENTER)    
    root.grid_columnconfigure(0, weight = 1)
    tree.pack(expand=True,fill=BOTH)

    try:
        cur.execute("SELECT t.title, a.artist_name, al.album_name, l.language_name, t.rlsyr FROM track t JOIN album al ON t.album_id=al.id JOIN artist a ON t.artist_id=a.id JOIN genre g ON t.genre_id=g.id JOIN language l ON t.language_id=l.id WHERE l.language_name != 'hindi' AND l.language_name != 'telugu' AND l.language_name != 'odissi' AND l.language_name != 'english';")
        rows = cur.fetchall()
        con.commit()
        
        for i in rows:
            tree.insert("", tk.END, values=i)
            
    except:
        messagebox.showinfo('Error',"Failed To Fetch Songs From The Database")

    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
   
   
def viewlanguage(): 
 
    root = Toplevel()
    root.title("View Languages")
    root.minsize(width=1366,height=768)
    root.geometry("1366x768")
    mypass = "abcd@1234"
    mydatabase="python_songs"
    con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
    cur = con.cursor()
    background_image = Image.open("./images/lang.jpg")
    background_image = ImageTk.PhotoImage(background_image)
    
    background_label = Label(root, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    root.minsize(width=1366,height=768)
    headingFrame1 = Frame(root, bg="black", bd=5)
    headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
        
    headingLabel = Label(headingFrame1, text="View Languages",font='Helvetica 14 bold', bg="white", fg='black',)
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    btn1 = Button(root,text="Hindi",font='Helvetica 10 bold',bg='black', fg='white', command= lambda: viewlang("hindi"))
    btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
    btn2 = Button(root,text="Odissi",font='Helvetica 10 bold',bg='black', fg='white', command= lambda: viewlang("odissi"))
    btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    
    btn3 = Button(root,text="Telugu",font='Helvetica 10 bold',bg='black', fg='white', command= lambda: viewlang("telugu"))
    btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
    
    btn4 = Button(root,text="English",font='Helvetica 10 bold',bg='black', fg='white', command= lambda: viewlang("english"))
    btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)
    
    btn5 = Button(root,text="Other Languages",font='Helvetica 10 bold',bg='black', fg='white', command=otherlang)
    btn5.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)
    
    root.mainloop()