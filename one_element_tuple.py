import sqlite3

conn = sqlite3.connect('test.db')


with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_txt(\
                ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                col_txt TEXT \
                )")
    conn.commit()

conn = sqlite3.connect('test.db')

fileList = ('information.docx' 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto,jpg')

for x in fileList:
    if x.endswith('txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_txt (col_txt) VALUES (?)", (x,))
            print(x)

conn.close()