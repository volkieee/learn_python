from services import db4
from library import library1


  
def display_jadwal_dan_kursi():
    while True:
        add_film = input("ingin menambahkan film?[y/n]: ").lower()
        if add_film == "y" or add_film == "n":
            break  # Keluar dari loop jika jawaban sudah valid ('y' atau 'n')
        else:
            print("❌ Pilihan salah! Masukkan hanya 'y' atau 'n'")
    if add_film=="y":    
        while True:
            print("\n--input data film--")
            judul=input("judul film:")
            harga=input("harga film:")
            db4.input_film(judul,harga)
            while True:
                tambah_film=input("ingin menambah film lagi?[y/n]:")
                if tambah_film=="y" or tambah_film=="n":
                    break
                else:
                    print("Pilihan salah! Masukkan hanya 'y' atau 'n'")
            if tambah_film=="y":
                continue
            else:
                break               
    library1.welcome_jadwalFilm()
    seat=db4.denah_kursi()
    # if len(seat)=0 kayak 
    if len(seat)==0:
        daftar_kursi = [
            "A1", "A2", "A3",
            "B1", "B2", "B3",
            "C1", "C2", "C3",
            "D1", "D2", "D3",
            "E1", "E2", "E3"
        ]
        # # Membuka cursor dari koneksi database di db4
        cursor=db4.db.cursor()
        for nama in daftar_kursi:
            pass
    
    print("daftar film yang tayang:")
    isi_film=db4.jadwal_film()
    for film in isi_film:
        id_film=film[0]
        judul=film[1]
        harga=film[2]
        print(f"[ ID: {id_film} ] {judul:<25} | Harga: Rp {harga}")
    print("-"*30)
    
    
    

def booking_seat():
    nama_pembeli=input("Masukkan nama anda:")
    id_film=int(input("Massukan id film:"))
    id_kursi=int(input("Masukkan id kursi (1-12):"))
    db4.book_tiket(nama_pembeli,id_film,id_kursi)
    
 
library1.welcome_CinemaApp()
while True:
    menu=int(input("\n1.Lihat Jadwal Film & Denah Kursi\n2.Pesan Tiket (Booking)\n3.Cetak Tiket Penonton\n4.Batalkan Pesanan (Refund)\n5.Keluar Aplikasi\n\nSilahkan di pilih:"))
    
    if menu==1:
        display_jadwal_dan_kursi()  
    elif menu==2:
        booking_seat()
    elif menu==3:
        pass
    elif menu==4:
        pass
    elif menu==5:
        pass
    