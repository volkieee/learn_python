import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from library import library1
from services import db2
import main
def add():
    Judul=input("Judul Buku:")
    Penulis=input("Penulis:")
    Tahun=int(input("Tahun:"))
    Status=input("Status:")
    
    db2.insert_table(Judul,Penulis,Tahun,Status)
    
def check():
    text="Daftar Buku Perpus"
    width=len(text)+70
    style="="*width
    print(style)
    print(text.center(width))
    print(style)
    items=db2.fetch_item()
    for item in items:
        id_buku=item[0]
        Judul=item[1]
        Penulis=item[2]
        Tahun=item[3]
        Status=item[4]
        print(f"[ID: {id_buku}]  Judul: {Judul}  | Penulis: {Penulis}  | Thn: {Tahun} | Status: {Status}")
        
def borrow():
    id_buku=input("Masukkan ID buku yang ingin dipinjam: ")
    cursor=db2.db.cursor()
    cursor.execute("UPDATE tbl_buku SET Status='Dipinjam' WHERE id=%s",(id_buku,))
    db2.db.commit()
    print("\nStatus buku berhasil dijadikan 'DiPinjam'\n")
    
def delete():
    id_buku=input("Masukkan iD buku yang ingin dihapus:")
    cursor=db2.db.cursor()
    cursor.execute("DELETE FROM tbl_buku WHERE id=%s",(id_buku,))        
    db2.db.commit()
    print("\nBuku berhasil dihapus\n")
        

def start():
    library1.welcome_message2()
    while True:
        menu=int(input("menu\n1.Tampilkan Semua Buku\n2.Tambah Buku baru\n3.Pinjam buku\n4.Hapus Buku\n5.exit\n\nSilahkan dipilih:"))
        if menu==1:
            check()
        elif menu==2:
             add()
        elif menu==3:
            borrow()
        elif menu==4:
            delete()         
        elif menu==5:
            main.menu()
            
if __name__=="__main__":
    start()            