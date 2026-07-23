import socket
from time import sleep
pc_name=socket.gethostname()

def welcome_message():
    style="*" * (len(pc_name)+6)
    print(style)
    print(f"** {pc_name} **")
    print(style)
    
def welcome_message2():
    text="WELCOME TO MINI LIBRARY"
    width=len(text)+10
    style="="*width
    print(style)
    print(text.center(width)) 
    print(style)   

def exit_program():
    print("Program akan dihentikan  ")
    sleep(1)
    print("3..")
    sleep(1)
    print("2..")
    sleep(1)
    print("1..")
    sleep(1)
    print("Program di hentikan")
    exit()
    
    
def welcome_message_nilaiRaporSiswa():
    text="SISTEM NILAI RAPOR SISWA"
    width=len(text)+10
    style="="*width    
    print(style)
    print(text.center(width))
    print(style)
    
def exit_program2():
    print("Program akan di hentikan dalam hitungan")
    sleep(1)
    print("3..")    
    sleep(1)
    print("2..")    
    sleep(1)
    print("1..")
    print("Program dihentikan")
    exit()    
      
def welcome_dataRapor():
    text="Data Rapor Siswa"
    width=len(text)+50
    style="="*width
    print(style)     
    print(text.center(width))
    print(style)   
    
    
    
def welcome_jadwalFilm():
    text="Jadwal Film & Denah Kursi"
    width=len(text)+50
    style="="*width
    print(style)
    print(text.center(width))
    print(style)
          
def welcome_CinemaApp():
    text="WELCOME TO CINEMA APP"
    width=len(text)+50
    style="="*width
    print(style)          
    print(text.center(width))
    print(style)
    
    
    
    
    
def welcome_message_rental_motor():
    text="APLIKASI RENTAL MOTOR"     
    width=len(text)+10
    style="="*width
    print(style)
    print(text.center(width))    
    print(style)
    return width    
    # Kita return nilai width-nya agar fungsi cetak menu di bawah 
    # bisa menyesuaikan panjang garis pembatasnya secara otomatis
             
def menu_rental_motor(width):
    style="-"*width       
    print("1.Daftar Motor & Harga")
    print("2.Sewa Motor (Input Pesanan)")
    print("3.Pengembalian Motor (Selesai Sewa)")
    print("4.Lihat Riwayat Sewa")
    print("5.Keluar Aplikasi")
    print(style)  
def list_rental_motor():
    text="Daftar Motor"
    width=len(text)+50
    style="="*width
    print(style)          
    print(text.center(width))
    print(style)       
if __name__=='__main__':
    # welcome_dataRapor()
    # welcome_message_nilaiRaporSiswa()
    # welcome_message2()
    # welcome_message()    
    # exit_program()
    welcome_message_rental_motor()
    
    