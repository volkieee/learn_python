import mysql.connector

db=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='raport siswa'
)

def insert_table_siswa(Nama,Kelas):
    cursor=db.cursor()
    cursor.execute("INSERT INTO tbl_siswa (Nama,Kelas) VALUES(%s,%s)",(Nama,Kelas))
    db.commit()
    if cursor.rowcount>0:
        print("\nSiswa berhasil ditambahkan\n")
    else:
        print("\nSiswa gagal ditambahkan\n")
        
def insert_table_nilai(id_siswa,mapel,nilai_tugas,nilai_uts,nilai_uas):
    cursor=db.cursor()
    cursor.execute("INSERT INTO tbl_nilai (id_siswa,mapel,nilai_tugas,nilai_uts,nilai_uas) VALUES(%s,%s,%s,%s,%s)",(id_siswa,mapel,nilai_tugas,nilai_uts,nilai_uas))  
    db.commit()
    if cursor.rowcount>0:
       print("\nnilai berhasil dimasukkan\n") 
       
    else:
        print("\nnilai gagal dimasukkan\n")    
def insert_siswaById(id_siswa):
    cursor=db.cursor()
    cursor.execute("SELECT * FROM tbl_siswa WHERE id_siswa=%s",(id_siswa,)) 
    siswa=cursor.fetchone()           
    # fetchone itu untuk Mengambil 1 baris hasil pencarian
    cursor.close()
    return siswa

def ambil_semua_rapor_siswa():
    cursor=db.cursor()
    sql='''
    SELECT
        tbl_siswa.id_siswa,
        tbl_siswa.nama,
        tbl_siswa.kelas,
        tbl_nilai.mapel,
        tbl_nilai.nilai_tugas,
        tbl_nilai.nilai_uts,
        tbl_nilai.nilai_uas
    FROM tbl_nilai
    INNER JOIN tbl_siswa ON tbl_nilai.id_siswa=tbl_siswa.id_siswa
    ORDER BY tbl_siswa.id_siswa ASC
    '''
    cursor.execute(sql)
    semua_data=cursor.fetchall()
    cursor.close()
    return semua_data
    



            
    
    