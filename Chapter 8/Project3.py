listA= []
banyak= int(input("Masukkan Jumlah Mahasiswa= "))

x = 0
for x in range (0,banyak):
    x += 1
    nama = str(input("Masukan nama mahasiswa ke-"+ str(x) + " = "))
    t = 0
    for x in nama :
        t += 1
    karakter = nama + "(" + str(t) + " karakter)"
    listA.append(karakter)

#output
print("Pendataan mahasiswa")
listA.sort()
for y in listA:
    print(y)
