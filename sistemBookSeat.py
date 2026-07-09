from services import db4
from library import library1
from time import sleep

  
def display_jadwal_dan_kursi():
    while True:
        add_film = input("ingin menambahkan film?[y/n]:").lower()
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
    # JADWAL FILM
    print("daftar film yang tayang:")
    isi_film=db4.jadwal_film()
    for film in isi_film:
        id_film=film[0]
        judul=film[1]
        harga=film[2]
        print(f"[ ID: {id_film} ] {judul:<25} | Harga: Rp {harga}")
    print("-"*65)
    
    # DENAH KURSI
    print("Status Denah kursi")
    print("-"*65)
    isi_kursi=db4.denah_kursi()
    hitung=0
    for kursi in isi_kursi:
        id_kursi=kursi[0]
        nomor_kursi=kursi[1]
        status=kursi[2]
        print(f" [ID:{id_kursi:<2}|{nomor_kursi}:{status:<6}]  ",end="")
        # fungsi end itu buat ksh enter setelah kodenya di eksekusi
        hitung +=1 
        if hitung %3==0:
            print()   
    
def booking_seat():
    nama_pembeli=input("Masukkan nama anda:")
    id_film=int(input("Massukan id film:"))
    id_kursi=int(input("Masukkan id kursi (1-12):"))
    db4.book_tiket(nama_pembeli,id_film,id_kursi)
    sleep(1)
    
 
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
    