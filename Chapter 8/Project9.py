try:
    print("Daftar harga buah per kilogram: ")
    listbuah ={"apel" : 5000, "jeruk" : 8500, "mangga" : 7800, "duku" :6500}
    
    sum = 0
    for a,b in listbuah.items():
        sum += 1
        print(sum ,".", a ,"=",b)

    buah = input("\nNama buah yang dibeli  : ")
    if(buah in listbuah):
        kg = float(input("Berapa Kg              : "))
        print("--------------------------------")
        print("Total harga            :",listbuah[buah]*kg)
    else:
        print(buah, "tidak terdapat di daftar buah")
except ValueError:
    print('Data yang anda masukan bukan angka')
