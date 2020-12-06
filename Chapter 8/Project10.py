try:
    print("Daftar harga buah per kilogram: ")
    listbuah ={"apel" : 5000, "jeruk" : 8500, "mangga" : 7800, "duku" :6500}
    
    sum = 0
    for a,b in listbuah.items():
        sum += 1
        print(sum ,".", a ,"=",b)

    jumlah = 0
    x = 'y'
    while x == 'y':
        buah = input("\nNama buah yang dibeli  : ")
        if(buah in listbuah):
            kg = float(input("Berapa Kg              : "))
            jumlah += (listbuah[buah]*kg)
            x = str(input('Beli buah yang lain (y/n)? '))
        else:
            print(listbuah, "tidak terdapat di daftar buah")
            break
        
    print("--------------------------------")
    print('Total Harga            : ', jumlah)
except ValueError:
    print('Data yang anda masukan bukan angka')
    
