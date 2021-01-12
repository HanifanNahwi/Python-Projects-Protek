def getUsia(tgl):
    import datetime
    time = datetime.datetime.now()
    from datetime import datetime
    konver = datetime.strptime(tgl, "%Y-%m-%d")
    rumus = konver - time
    umur = int(rumus.days)
    umur = abs(umur/365)
    import math
    umur = math.floor(umur)
    umur = str(umur)
    return umur

def addKaryawan(nip,nama,alamat,gol,tgllhr):
    data = open("dataKaryawan.dat", "a+")
    data.write(nip + "|" + nama + "|" + alamat + "|" + gol + "|" + tgllhr + "|" + getUsia(tgllhr) + "\n")


nip = str(input("Masukkan NIP        : "))
nama = str(input("Masukkan Nama       : "))
alamat = str(input("Masukkan Alamat     : "))
gol = str(input("Masukkan Golongan   : "))
a = ["A","B","C"]
if gol not in a:
    print("golongan tidak sesuai")
    exit()
tgllhr = str(input("Masukkan Tgl Lahir  (TTTT-BB-HH): "))

getUsia(tgllhr)
addKaryawan(nip,nama,alamat,gol,tgllhr)
