kodekaryawan     = int(input("Masukkan kode Karyawan              : "))
namakaryawan     = str(input("Masukkan Nama Karyawan              : "))
golongankaryawan = str(input("Masukkan Golongan                   : "))
menikah          = int(input("Masukkan status (1:Menikah, 2:Belum): "))

if(menikah == 1):
    statusnya = "Menikah"
    anak      = int(input("Masukkan Jumlah Anak                : "))
else:
    statusnya = "Belum"

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

#Tunjangan
if (statusnya == "Menikah"):
    Tistri = gajipokok * 10/100
    Tanak  = anak * gajipokok * 5/100
#gaji kotor dan bersih
if (statusnya == "Menikah"):
    gkotor = gajipokok + Tistri + Tanak
elif (statusnya == "Belum"):
    gkotor = gajipokok

potongangaji = int(gajipokok*(potongan/100))

print("=====================================")
print("     STRUK RINCIAN GAJI KARYAWAN     ")
print("=====================================")
print("Nama Karyawan  :",namakaryawan)
print("Kode Karyawan  :",kodekaryawan)
print("Golongan       :",golongankaryawan)
print("Status         :",statusnya)
if(statusnya == "Menikah"):
    print("Jumlah Anak    :",anak)
print("-------------------------------------")
print("Gaji Pokok     : Rp.",gajipokok)
if(statusnya == "Menikah"):
    print("Tunjangan Istri: Rp.",int(Tistri))
    print("Tunjangan Anak : Rp.",int(Tanak))
print("Potongan({0}%) : Rp. ({1}) ".format(potongan,potongangaji))
print("-------------------------------------")
print("Gaji Bersih    : Rp.",(int(gkotor-potongangaji)))
