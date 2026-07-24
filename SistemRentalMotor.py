from library import library1
from services import dbRentalMotor

def input_daftar_motor():
    while True:
        tanya_awal=input("ingin menambahkan motor?[y/n]:")
        if tanya_awal in ["y","n"]:
             break
        print("isi yang benar[y/n]")
    if tanya_awal=="y":
            while True:
                merek_motor=input("Merek motor:")
                plat_nomor=input("Plat nomor:")
                harga_per_hari=int(input("Harga/hari:"))
                status_awal="Tersedia"
                dbRentalMotor.insert_motor(merek_motor,plat_nomor,harga_per_hari,status_awal)
                while True:   
                    break_loop=input("ingin menambahkan motor lagi?[y/n]:").strip()
                    if break_loop in["y","n"]:
                        break
                    print("Tolong isi dgn benar [y/n]:")
                if break_loop=="n":
                    print("Selesai menambahkan data motor")
                    break
    library1.list_rental_motor()
    data_motor = dbRentalMotor.list_motor()
# Cetak setiap baris motor (sama persis gaya penulisan kode film kamu)
    for data in data_motor:
        id_motor=data[0]
        merek = data[1]
        plat_nomor = data[2]
        harga_per_hari = data[3]
        status = data[4]
        print(f"ID:{id_motor:<2} | Merek motor: {merek:<8} | Plat: {plat_nomor:<10} | Harga: Rp {harga_per_hari:<8,} | Status: {status}")
    print("-" * 80)
            

length=library1.welcome_message_rental_motor()
while True:
    library1.menu_rental_motor(length)
    option=int(input("Pilih menu[1-5]:").strip())
    # .strip() agar misal Teks " 1 " otomatis dibersihkan menjadi "1". Spasi gaib di kanan-kirinya langsung dibuang jadi logic if akan aman dan tetap berjalan lancar.
    if option==1:
        input_daftar_motor()
    elif option==2:
        pass
    elif option==3:
        pass
    elif option==4:
        pass
    elif option==5:
        library1.exit_program()