from library import library1
from services import dbRentalMotor

def input_daftar_motor():
    merek_motor=input("Merek motor:")
    plat_nomor=input("Plat nomor:")
    harga_per_hari=int(input("Harga/hari:"))
    status_awal="tersedia"
    dbRentalMotor.insert_motor(merek_motor,plat_nomor,harga_per_hari,status_awal)






length=library1.welcome_message_rental_motor()
while True:
    library1.menu_rental_motor(length)
    option=int(input("Pilih menu[1-5]:").strip())
    # .strip() agar misal Teks " 1 " otomatis dibersihkan menjadi "1". Spasi gaib di kanan-kirinya langsung dibuang jadi logic if akan aman dan tetap berjalan lancar.
    if option==1:
        pass
    elif option==2:
        pass
    elif option==3:
        pass
    elif option==4:
        pass
    elif option==5:
        library1.exit_program()