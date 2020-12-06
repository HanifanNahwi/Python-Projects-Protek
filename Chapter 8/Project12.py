listbuah ={"apel" : 5000, "jeruk" : 8500, "mangga" : 7800, "duku" :6500}
def menampilkan(x):
    print("Daftar harga Buah per kilogram: ")
    sum = 0
    for a,b in listbuah.items():
        sum += 1
        print(sum ,".", a ,"=",b)
menampilkan(listbuah)

while True:
    menu = ["\nMenu:",
    "A. Tambah data buah",
    "B. Beli buah",
    "C. Tutup program",
    "D. Hapus data buah"]
    for i in menu:
        print(i)
    print('-------------------------')
    pil = input('pilihan menu (A/B/C/D) : ')
    print('-------------------------\n')

    if pil == 'A':
        while True:
            a = input('Masukkan nama buah   : ')
            if (a in listbuah):
                print('Buah sudah ada di dalam dictionary')
            else:
                harga = int(input("Harga buah           : "))
                listbuah[a] = harga
                print("\nperubahan data buah")
                menampilkan(listbuah)
                tambah = str(input("Mau menambahkan lagi(y/n)? "))
                if tambah == "y":
                    print("perubahan data buah = ", buah)
                elif tambah == "n":
                    break
    elif pil == 'B':
        jumlah = 0
        x = 'y'
        while x == 'y':
            buah = input("\nNama buah yang dibeli  : ")
            if(buah in listbuah):
                kg = float(input("Berapa Kg              : "))
                jumlah += (listbuah[buah]*kg)
                x = str(input('Beli buah yang lain (y/n)? '))
                if x == 'n':
                    print("---------------------------------")
                    print('Total Harga            : ', jumlah)
                    print("---------------------------------\n")
            else:
                print(listbuah, "tidak terdapat di daftar buah")
    elif pil == 'C':
        print('Terima kasih')
        break
    elif pil == 'D':
        a = input('Nama buah yang ingin dihapus : ')
        if(a not in listbuah):
            print(a, 'tidak ditemukan')
        else:
            del(listbuah[a])
            print(a, 'telah dihapus\n')
            menampilkan(listbuah)
            


    
