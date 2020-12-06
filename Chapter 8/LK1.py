#1. List
a = [1, 5, 6, 3, 6, 9, 11, 20, 12]
b = [7, 4, 5, 6, 7, 1, 12, 5, 9]
print('\n-------No.1-------')
print(a, b)

#2. Menyisipkan
a.insert(3, 10)
b.insert(2, 8)
print('\n-------No.2-------')
print(a, b)

#3. Menyisipkan ke indeks terakhir
a.append(4)
b.append(8)
print('\n-------No.3-------')
print(a, b)

#4. Sorting
a.sort()
b.sort()
print('\n-------No.4-------')
print(a, b)

#5. list yang elemennya adalah sublist dari list sebelumnya
c = a[0:7]
d = b[2:9]
print('\n-------No.5-------')
print(c, d)

#6. list yang elemennya adalah penjumlahan dari list sebelumnya
e = []
x = 0
for x in range(len(c)):
    y = c[x] + d[x]
    e = e + [y]
print('\n-------No.6-------')
print(e)

#7. list ke dalam Tuple
E = tuple(e)
print('\n-------No.7-------')
print(E)

#8. nilai max, min, dan jumlah dari tuple
nilaimax = max(E)
nilaimin = min(E)
jumlah = sum(E)
print('\n-------No.8-------')
print("A. Nilai Maks   = ", nilaimax)
print("B. Nilai Min    = ", nilaimin)
print("C. Nilai Jumlah = ", jumlah)

#9. variable yang berisi string
myString = "python adalah bahasa pemrograman yang menyenangkan"
print('\n-------No.9-------')
print(myString)

#10. karakter huruf apa saja yang terdapat pada string menggunakan set
karakter = set(myString)
print('\n-------No.10-------')
print("Karakter hurufnya= ", karakter)

#11. string ke list lalu di urutkan 
kelist = list(karakter)
kelist.sort()
print('\n-------No.11-------')
print("11' Karakter huruf setelah diurutkan= ", kelist)

