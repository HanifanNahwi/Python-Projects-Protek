from datetime import *
file = open("DataPeminjam.txt", 'a+')
while True :   
    kode = input("Masukkan Kode Member : ")
    nama = input("Masukkan Nama Member : ")
    judul = input("Masukkan Judul Buku  : ")

    skrg = date.today()
    kembali = skrg + timedelta(days = 7)
    file.write(kode + "|" + nama + "|" + judul + "|" + str(skrg) + "|" + str(kembali) + "\n")
    pil = input('\nUlangi lagi? (y/n) : ')
    if pil == 'y' :
        continue  
    elif pil == 'n' :
        break
    else :
        print("Input Anda Salah")
        break
file.close()
