import mysql.connector

db=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='book_seat'   
)

def input_film(judul,harga):
    cursor=db.cursor()
    cursor.execute("INSERT INTO tbl_film (judul,harga) VALUES(%s,%s)",(judul,harga))
    db.commit()
    
    if cursor.rowcount>0:
        print("data film berhasil di masukkan")
    else:
        print("data film gagal di masukkan")
    cursor.close()
        
            
def jadwal_film():
    cursor=db.cursor()
    cursor.execute("SELECT id_film,judul,harga FROM tbl_film")
    show_film=cursor.fetchall()
    cursor.close()
    return show_film

def denah_kursi():
    cursor=db.cursor()
    cursor.execute("SELECT id_kursi,nomor_kursi,status FROM tbl_kursi")
    show_seat=cursor.fetchall()
    cursor.close()
    return show_seat
    
def book_tiket(nama_pembeli,id_film,id_kursi):
    cursor=db.cursor()
    cursor.execute("INSERT INTO tbl_pesanan(nama_pembeli,id_film,id_kursi) VALUES (%s,%s,%s)",(nama_pembeli,id_film,id_kursi))
    db.commit()
    if cursor.rowcount>0:
        print("data berhasil di masukkan")
    else:
        print("data gagal di masukkan")    
    