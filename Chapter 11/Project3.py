from datetime import *
def diffDate(x):
    x = datetime.strptime(x,'%Y-%m-%d').date()
    y = datetime.date(datetime.now())
    z = y - x
    return int(z.days)

from datetime import *
file = open("DataPeminjam.txt", "r")
list1 = []
list2 = []
list3 = []
list4 = []
list5 = []

for i in file:
    a = i.split("|")
    list1.append(a[0])
    list2.append(a[1])
    list3.append(a[2])
    list4.append(a[3])
    list5.append(a[4].strip())

search = str(input("Masukkan Kode Member      : "))
if search in list1:
    status = 'ada'
    a = list1.index(search)
    x = list5[a]
    y = diffDate(x)
    pengembalian = datetime.date(datetime.now())  
    if status == 'ada':
        if(y <= 0) :      
            terlambat = "Tidak Terlambat"
            denda = "Tidak Ada Denda"     
        elif(y > 0) :   
           terlambat = str(y) + " hari"
           denda = "Rp " + str(y*2000)
        print("\nData Peminjaman Buku\n"
             "\nKode Member                    : ",list1[a],
             "\nNama Member                    : ",list2[a],
             "\nJudul Buku                     : ",list3[a],
             "\nTanggal Mulai Peminjaman       : ",list4[a],
             "\nTanggal Maks Peminjaman        : ",list5[a],
             "\nTanggal Pengembalian           : ",pengembalian,
             "\nKeterlambatan                  : ",terlambat,
             "\nTotal denda                    : ",denda)

else:
    print("Data Tidak Ditemukan")
        
    
