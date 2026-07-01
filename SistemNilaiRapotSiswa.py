from services import db3
from library import library1

def add():
    Nama=input("Nama:")
    Kelas=input("Kelas:")
    
    db3.insert_table_siswa(Nama,Kelas)
    
def input_id_siswa():
    id_siswa=int(input("Masukkan Id Siswa:"))    
    data=db3.insert_siswaById(id_siswa) 
    if data is not None:
        print(f"Nama  : {data[1]}")  # Index 0 itu kolom Nama
        print(f"Kelas : {data[2]}")  # Index 1 itu kolom kelas
        print("-" * 30)
        mapel=input("Masukkan Mata Pelajaran:")    
        tugas=int(input("Masukkan Nilai Tugas:"))
        uts=int(input("Masukkan Nilai UTS:"))
        uas=int(input("Masukkan Nilai UAS:"))
        db3.insert_table_nilai(id_siswa,mapel,tugas,uts,uas)
        
        nilai_akhir=(0.3*tugas)+(0.3*uts)+(0.4*uas)
        if nilai_akhir>=75:
            status="LULUS"
        else:
            status="TIDAK LULUS"
            
        print("-" * 30)
        print(f"Hasil Hitung Otomatis untuk Mapel {mapel}:")
        print(f"➡️ Nilai Akhir : {nilai_akhir:.1f}")
        print(f"➡️ Status      : {status}")
        print("-" * 30)    
    else:
        # Kalau ID siswa tidak ada di database
        print(f"❌ Siswa dengan ID {id_siswa} tidak ditemukan!")
    
def tampilkan_semua_rapor():
    library1.welcome_dataRapor()
    data_rapor=db3.ambil_semua_rapor_siswa()
    if len(data_rapor)==0:
        print("belum ada data nilai siswa yang di input kedalam data base")
    else:
        print(f"{'ID':<5}{'Nama Siswa':<20}{'Kelas':<8}{'Mapel':<15}{'Akhir':<10}{'Status':<10}")
        print("-" * 73)
        
    for baris in data_rapor:
        id_siswa=baris[0]
        nama=baris[1]
        kelas=baris[2]
        mapel=baris[3]
        tugas=baris[4]
        uts=baris[5]
        uas=baris[6]
        
        nilai_akhir = (0.3 * tugas) + (0.3 * uts) + (0.4 * uas)
            
            # Tentukan Status Kelulusan
        if nilai_akhir >= 75:
                status = "LULUS"
        else:
                status = "REMEDI"
                
            # Cetak datanya ke samping sesuai kolom header
        print(f"{id_siswa:<5}{nama:<20}{kelas:<10}{mapel:<15}{nilai_akhir:<10.1f}{status:<10}")
            
        print("-" * 73)
        
    input("\n[Tekan Enter untuk kembali ke menu utama]")
        
def tampilkan_per_siswa():
    id_siswa = int(input("Masukkan id siswa: "))
    data = db3.ambil_rapor_per_siswa(id_siswa)
    
    # 1. Cek apakah datanya ada (list tidak kosong)
    if len(data) > 0:
        # Ambil baris pertama [0] untuk dasar mencetak Biodata
        baris_pertama = data[0] 
        
        print("\n" + "="*40)
        print(f"Nama  : {baris_pertama[1]}")  # Index 1 adalah Nama
        print(f"Kelas : {baris_pertama[2]}")  # Index 2 adalah Kelas
        print("="*40)
        
        # Cetak header untuk daftar nilai
        print(f"{'Mapel':<15}{'Tugas':<8}{'UTS':<8}{'UAS':<8}{'Akhir':<8}{'Status':<8}")
        print("-" * 50)
        
        # 2. Mulai looping untuk membongkar nilai mapelnya ke bawah
        for baris in data:
            mapel = baris[3]
            tugas = baris[4]
            uts   = baris[5]
            uas   = baris[6]
            
            nilai_akhir = (0.3 * tugas) + (0.3 * uts) + (0.4 * uas)
            status = "Lulus" if nilai_akhir >= 70 else "Tidak Lulus"
            print(f"{mapel:<15}{tugas:<8}{uts:<8}{uas:<8}{nilai_akhir:<8.1f}{status}")
            
        print("-" * 50)
        input("\n[Tekan Enter untuk kembali ke menu utama]")
        
    else:
        print(f"❌ Data siswa dengan ID {id_siswa} tidak ditemukan.")
        input("\n[Tekan Enter untuk kembali ke menu utama]")
while True:
    library1.welcome_message_nilaiRaporSiswa()
    menu=int(input("Menu\n1.Daftarkan Siswa Baru\n2.Input Nilai Mata Pelajaran\n3.Tampilkan Semua Rapor Siswa\n4.Cari Rapor per Siswa (Cetak Rapor)\n5.Keluar Aplikasi\n\nSilahkan dipilih:"))
    if menu==1:
        add()
    elif menu==2:
        input_id_siswa()    
    elif menu==3:
        tampilkan_semua_rapor()    
    elif menu==4:
        tampilkan_per_siswa()    
    elif menu==5:
        library1.exit_program2()    
    