import mysql.connector
from library import library1
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="rental_motor"
)


def insert_motor(merek,plat_nomor,harga_per_hari,status):
    cursor=db.cursor()
    cursor.execute("INSERT INTO tbl_motor (merek,plat_nomor,harga_per_hari,status) VALUES(%s,%s,%s,%s)",(merek,plat_nomor,harga_per_hari,status))
    db.commit()
    
    if cursor.rowcount>0:
        print("Data berhasil dimasukkan")
    else:
        print("Data gagal dimasukkan")
        
def list_motor():
    cursor=db.cursor()
    cursor.execute("SELECT id_motor,merek,plat_nomor,harga_per_hari,status FROM tbl_motor")
    show_list=cursor.fetchall()
    return show_list
        
       
