import pymysql

mydatabase = "python_songs"
mypass = "abcd@1234"

try:
    con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
    cur = con.cursor()
    
    cur.execute('''CREATE TABLE IF NOT EXISTS Artist(
                id INTEGER AUTO_INCREMENT,
                artist_name VARCHAR(50) UNIQUE,
                PRIMARY KEY(id));''')
    
    cur.execute('''CREATE TABLE IF NOT EXISTS Genre(
                id INTEGER AUTO_INCREMENT,
                genre_name VARCHAR(50) UNIQUE,
                PRIMARY KEY(id));''')
    
    cur.execute('''CREATE TABLE IF NOT EXISTS Album(
                id INTEGER AUTO_INCREMENT,
                album_name VARCHAR(50) UNIQUE,
                artist_id INTEGER,
                PRIMARY KEY(id),
                FOREIGN KEY(artist_id) REFERENCES Artist(id) ON DELETE CASCADE);''')
    
    cur.execute('''CREATE TABLE IF NOT EXISTS Language(
                id INTEGER AUTO_INCREMENT,
                language_name VARCHAR(50) UNIQUE,
                PRIMARY KEY(id));''')
    
    cur.execute('''CREATE TABLE IF NOT EXISTS Track(
                title VARCHAR(50) UNIQUE,
                album_id INTEGER,
                genre_id INTEGER,
                artist_id INTEGER,
                language_id INTEGER,
                rlsyr INTEGER,
                PRIMARY KEY(title),
                FOREIGN KEY(album_id) REFERENCES Album(id) ON DELETE CASCADE,
                FOREIGN KEY(genre_id) REFERENCES Genre(id) ON DELETE CASCADE,
                FOREIGN KEY(artist_id) REFERENCES Artist(id) ON DELETE CASCADE,
                FOREIGN KEY(language_id) REFERENCES Language(id) ON DELETE CASCADE);''')
    
    cur.execute("""
        CREATE OR REPLACE VIEW Tracks_by_Release_Year AS
        SELECT rlsyr, COUNT(*) as num_tracks
        FROM Track
        GROUP BY rlsyr;
    """)
    
    cur.execute("""
        CREATE OR REPLACE VIEW Albums_in_Languages AS
        SELECT l.language_name, COUNT(*) as num_albums
        FROM Track t
        JOIN Language l ON t.language_id = l.id
        JOIN Album al ON t.album_id = al.id
        GROUP BY l.language_name;
    """)
    
    cur.execute("""
        CREATE OR REPLACE VIEW Albums_in_Genres AS
        SELECT g.genre_name, COUNT(*) as num_albums
        FROM Track t
        JOIN Genre g ON t.genre_id = g.id
        JOIN Album al ON t.album_id = al.id
        GROUP BY g.genre_name;
    """)

    con.commit()
    print("Done Biscuit!")
except Exception as e:
    print("An error occurred: ", str(e))
