kodekaryawan = int(input("Masukkan kode Karyawan : "))
namakaryawan = str(input("Masukkan Nama Karyawan : "))
golongankaryawan = str (input("Masukkan Golongan      : "))

if(golongankaryawan == "A"):
    gajipokok = 10000000
    potongan = 2.5
elif(golongankaryawan == "B"):
    gajipokok = 8500000
    potongan = 2.0
elif(golongankaryawan == "C"):
    gajipokok = 7000000
    potongan = 1.5
elif(golongankaryawan == "D"):
    gajipokok = 5500000
    potongan = 1.0
else:
    print("Golongan Anda tidak ditemukan")
    exit()

potongangaji = gajipokok*(potongan/100)

print("=====================================")
print("     STRUK RINCIAN GAJI KARYAWAN     ")
print("=====================================")
print("Nama Karyawan  :",namakaryawan)
print("Kode Karyawan  :",kodekaryawan)
print("Golongan       :",golongankaryawan)
print("-------------------------------------")
print("Gaji Pokok     : Rp.",gajipokok)
print("Potongan({0}%) : Rp. ({1}) ".format(potongan,potongangaji))
print("-------------------------------------")
print("Gaji Bersih    : Rp.",(gajipokok-potongangaji))
