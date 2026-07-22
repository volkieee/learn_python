import mysql.connector

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
        