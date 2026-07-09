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
    cursor = db.cursor()
    
    # 1. Cek apakah tabel kursi masih kosong 
    cursor.execute("SELECT COUNT(*) FROM tbl_kursi")
    jumlah_data = cursor.fetchone()[0]
    
    # 2. Kalau kosong (0), isi list kursinya
    if jumlah_data == 0:
        daftar_kursi = [
            "A1", "A2", "A3",
            "B1", "B2", "B3",
            "C1", "C2", "C3",
            "D1", "D2", "D3"
        ]
        
        for nama in daftar_kursi:
            sql = "INSERT INTO tbl_kursi (nomor_kursi, status) VALUES (%s, %s)"
            val = (nama, "KOSONG")
            cursor.execute(sql, val)
        db.commit()
        print("[Database]: 12 Kursi awal (A1-D3) berhasil didaftarkan otomatis!")
    
    # 3. Ambil data (Baris ini sejajar lurus dengan IF di atas, bukan di dalam IF)
    cursor.execute("SELECT id_kursi, nomor_kursi, status FROM tbl_kursi")
    show_seat = cursor.fetchall()
    
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
    