def gajiP(a):
    if a == "A":
        b = "Rp 4.000.000"
    elif a == "B":
        b = "Rp 4.500.000"
    elif a == "C":
        b = "Rp 5.000.000"
    else:
        b = "Rp 0 (data salah)"
    return b

f = open("dataKaryawan.dat", "r") #mengambil data file.dat
dat = f.readlines()

print('='*90,"\nKODE KARY\tNAMA KARY     ALAMAT\t   GOL     GAJI POKOK\t     TGLLAHIR     USIA")
print('-'*90)
for i in dat:
    split = i.split("|")
    print(split[0],end="")     #nip
    a = len(split[0])
    print(split[1].rjust(25 - a),end="")    #nama
    a = len(split[2])
    print(split[2].rjust(5+a),end="")   #alamat
    a = len(split[2])
    print(split[3].rjust(15-a),end="")   #golongan
    print(gajiP(split[3]).rjust(18),end="")  #getGapok(split[3]) = mengambil gaji sesuai golongan
    print(split[4].rjust(16),end="")     # tanggal lahir
    print(split[5].rjust(6),end='')      #usia

print('-'*90)
