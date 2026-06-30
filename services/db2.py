import mysql.connector

db=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='mini_library'
)
cursor=db.cursor()
# inget klo execute itu panggil anaknya
def insert_table(Judul,Penulis,Tahun,Status):
    cursor=db.cursor()
    cursor.execute("INSERT INTO tbl_buku (Judul,Penulis,Tahun,Status) VALUES (%s,%s,%s,%s)",
                   (Judul,Penulis,Tahun,Status))
    db.commit()
    if cursor.rowcount>0:
        print("\nData berhasil di masukkan\n")
        
    else:
        print("\nData gagal di masukkan\n")    

def fetch_item():
    cursor=db.cursor()
    cursor.execute("SELECT * from tbl_buku")
    return cursor.fetchall()      
