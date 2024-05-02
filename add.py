from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql
from tkinter import Toplevel

def songadd():

    title = songInfo1.get()
    artist = songInfo2.get()
    album = songInfo3.get()
    genre = songInfo4.get()
    rlsyr = songInfo5.get()
    language = songInfo6.get()

    try:  
        cur.execute('SELECT id FROM artist WHERE artist_name = %s', (artist,))
        artist_id = cur.fetchone()
        if artist_id is None:
            cur.execute('INSERT INTO artist (artist_name) VALUES (%s)', (artist,))
            con.commit()
            cur.execute('SELECT id FROM artist WHERE artist_name = %s', (artist,))
            artist_id = cur.fetchone()[0]
        else:
            artist_id = artist_id[0]

        cur.execute('SELECT id FROM album WHERE album_name = %s', (album,))
        album_id = cur.fetchone()
        if album_id is None:
            cur.execute('INSERT INTO album (album_name) VALUES (%s)', (album,))
            con.commit()
            cur.execute('SELECT id FROM album WHERE album_name = %s', (album,))
            album_id = cur.fetchone()[0]
        else:
            album_id = album_id[0]

        cur.execute('SELECT id FROM genre WHERE genre_name = %s', (genre,))
        genre_id = cur.fetchone()
        if genre_id is None:
            cur.execute('INSERT INTO genre (genre_name) VALUES (%s)', (genre,))
            con.commit()
            cur.execute('SELECT id FROM genre WHERE genre_name = %s', (genre,))
            genre_id = cur.fetchone()[0]
        else:
            genre_id = genre_id[0]

        cur.execute('SELECT id FROM language WHERE language_name = %s', (language,))
        language_id = cur.fetchone()
        if language_id is None:
            cur.execute('INSERT INTO language (language_name) VALUES (%s)', (language,))
            con.commit()
            cur.execute('SELECT id FROM language WHERE language_name = %s', (language,))
            language_id = cur.fetchone()[0]
        else:
            language_id = language_id[0]

        cur.execute('INSERT INTO track (title, album_id, genre_id, artist_id, rlsyr, language_id) VALUES (%s, %s, %s, %s, %s, %s)', (title, album_id, genre_id, artist_id, rlsyr, language_id))
        con.commit()
        messagebox.showinfo('Success',"Song Added Successfully")
    except:
        messagebox.showinfo("Error","Can't Add Song Into Database")

    root.destroy()

def addsong():
    global img,songInfo1,songInfo2,songInfo3,songInfo4,songInfo5,songInfo6,Canvas1,con,cur,root
    root = Toplevel()
    root.title("Add Music Record")
    root.minsize(width=1366,height=768)
    root.geometry("1366x768")

    mypass = "abcd@1234"
    mydatabase="python_songs"

    con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
    cur = con.cursor()

    background_image = Image.open("./images/add.jpg")
    [imageSizeWidth, imageSizeHeight] = background_image.size
    newImageSizeWidth = int(imageSizeWidth*0.7)
    newImageSizeHeight = int(imageSizeHeight*0.7)
    background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.BILINEAR)
    img = ImageTk.PhotoImage(background_image)

    Canvas1 = Canvas(root)
    Canvas1.create_image(300,340,image = img)
    Canvas1.config(bg="white", width = newImageSizeWidth, height = newImageSizeHeight)
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="#2f2e2e",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Song Record",font='Helvetica 14 bold', bg= "#d7a26c", fg='black', )
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg="#d7a26c")
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)

    lb1 =Label(labelFrame, text="Title:", font='Helvetica 13 bold',bg="#d7a26c", fg='black')
    lb1.place(relx=0.05,rely=0.07, relheight=0.08)

    songInfo1 = Entry(labelFrame)
    songInfo1.place(relx=0.3,rely=0.07, relwidth=0.62, relheight=0.08)

    lb2 = Label(labelFrame,text="Artist:", font='Helvetica 13 bold',bg="#d7a26c", fg='black')
    lb2.place(relx=0.05,rely=0.07+(.16*1), relheight=0.08)

    songInfo2 = Entry(labelFrame)
    songInfo2.place(relx=0.3,rely=0.07+(.16*1), relwidth=0.62, relheight=0.08)

    lb3 = Label(labelFrame,text="Album:", font='Helvetica 13 bold',bg="#d7a26c", fg='black')
    lb3.place(relx=0.05,rely=0.07+(.16*2), relheight=0.08)

    songInfo3 = Entry(labelFrame)
    songInfo3.place(relx=0.3,rely=0.07+(.16*2), relwidth=0.62, relheight=0.08)

    lb4 = Label(labelFrame,text="Genre:", font='Helvetica 13 bold',bg="#d7a26c", fg='black')
    lb4.place(relx=0.05,rely=0.07+(.16*3), relheight=0.08)

    songInfo4 = Entry(labelFrame)
    songInfo4.place(relx=0.3,rely=0.07+(.16*3), relwidth=0.62, relheight=0.08)

    lb5 = Label(labelFrame,text="Release Year:", font='Helvetica 13 bold',bg="#d7a26c", fg='black')
    lb5.place(relx=0.05,rely=0.07+(.16*4), relheight=0.08)

    songInfo5 = Entry(labelFrame)
    songInfo5.place(relx=0.3,rely=0.07+(.16*4), relwidth=0.62, relheight=0.08)

    lb6 = Label(labelFrame,text="Language:", font='Helvetica 13 bold',bg="#d7a26c", fg='black')
    lb6.place(relx=0.05,rely=0.07+(.16*5), relheight=0.08)

    songInfo6 = Entry(labelFrame)
    songInfo6.place(relx=0.3,rely=0.07+(.16*5), relwidth=0.62, relheight=0.08)

    SubmitBtn = Button(root,text="Submit",font='Helvetica 12 bold',bg='#d7a26c', fg='black',command=songadd)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)

    quitBtn = Button(root,text="Quit",font='Helvetica 12 bold',bg='#d7a26c', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

    root.mainloop()