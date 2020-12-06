def sortStringByChar(a):
     a.sort(reverse=True, key=len)
     return(a)

n = int(input("Berapa banyaknya Buah : "))
data = []
for i in range(0, n):
    x = str(input("Masukkan buah ke-%d: " % (i+1)))
    data.append(x)

print("\nHasil buah dari list",data,'dengan urutan dari jumlah karakter penyusun tiap string huruf besar ke kecil :')
hasil = sortStringByChar(data)
print(hasil)
