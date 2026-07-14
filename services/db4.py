import mysql.connector
import datetime


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
        text="Data berhasil dimasukkan"
        width=len(text)+10
        style="="*width
        print(style)
        print(text.center(width))
        print(style)
        cursor.execute("UPDATE tbl_kursi SET status='TERISI' where id_kursi=%s",(id_kursi,))
        db.commit()
        cursor.close()
    else:
        print("Data gagal di masukkan")    
        
    cursor.close()
    
def cetak_tiket(nama_pembeli,judul_film,nomor_kursi,harga_film):
    time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    print("\n" + "="*50)
    print("🎟️               CINEMA TIKET XXI             🎟️")
    print("="*50)
    print(f" Waktu Transaksi : {time}")
    print("-"*50)
    print(f" 🎬 JUDUL FILM   : {judul_film.upper()}")
    print(f" 👤 PENONTON     : {nama_pembeli.upper()}")
    print(f" 💺 NOMOR KURSI  : {nomor_kursi}")
    print(f" 💵 HARGA        : Rp {harga_film}")
    print("-"*50)
    print("       TERIMA KASIH TELAH MEMBELI TIKET       ")
    print("      SILAHKAN DIBAWA KE GERBANG BIOSKOP       ")
    print("="*50 + "\n")
    
def ambil_tiket(nama_pembeli,id_film,id_kursi):
    cursor=db.cursor()
    cursor.execute("SELECT judul,harga FROM tbl_film WHERE id_film=%s",(id_film,))
    # itu film_data isnya tuple contoh (rush hour,50000)
    film_data=cursor.fetchone()
    
    cursor.execute("SELECT nomor_kursi FROM tbl_kursi WHERE id_kursi=%s",(id_kursi,))
    kursi_data=cursor.fetchone()
    cursor.close()
    
    if film_data and kursi_data:
        judul=film_data[0]
        harga=film_data[1]
        nomor_kursi=kursi_data[0]
        cetak_tiket(nama_pembeli,judul,nomor_kursi,harga)
    else:
        print("Gagal mencetak tiket karena data tidak ditemukan")
        
def tampilan_cek_refund():
    time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M")  
    
    
    
    
      
def cek_dan_proses_refund(nama_pembeli,id_film,id_kursi):
    cursor=db.cursor()
    
    cursor.execute("SELECT nama_pembeli,id_film,id_kursi FROM tbl_pesanan WHERE nama_pembeli=%s AND id_film=%s AND id_kursi=%s",(nama_pembeli,id_film,id_kursi))
    data_film=cursor.fetchone()
    cursor.execute("SELECT nomor_kursi,status FROM tbl_kursi WHERE id_kursi=%s",(id_kursi,))
    # wajib memakai (,) kalo di satu variabel karena agar datanya dikira tuple oleh py (data)kalau tanpa koma py akan mengira data tersebut hanyalah integer 
    
    data_kursi=cursor.fetchone()
    cursor.close()
    if data_film and data_kursi:
        nama_pembeli=data_film[0]
        id_film=data_film[1]
        nomor_kursi=data_kursi[0]
        tampilan_cek_refund(nama_pembeli,id_film,nomor_kursi)
    else:
        print("gagal memproses refund")
    
    
    
    
    
    
