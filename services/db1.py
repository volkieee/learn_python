import mysql.connector

db =mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='mini_store'
)


def insert_item(kode_barang,nama_barang,harga_barang,stok_barang):
    cursor=db.cursor()
    # menjelaskan query ke database
    cursor.execute("INSERT INTO TBL_BARANG (kode_barang,nama_barang,harga_barang,stok_barang) VALUES (%s,%s,%s,%s)",
                   (kode_barang,nama_barang,harga_barang,stok_barang))
    # -------
    # setelah dijalakan save dengan permanen
    db.commit()
    # -------
    if cursor.rowcount>0:
        print("\nData berhasil di masukkan\n")
    else:
        print("\ndata gagal di insert\n")
        
def fetch_item():
    cursor=db.cursor()
    cursor.execute("SELECT * FROM tbl_barang")
    return cursor.fetchall() 
        
        
    
