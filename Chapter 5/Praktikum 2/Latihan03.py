a = 0
sum = 0
for i in range (100):
    if i % 2 == 1:
        a = a + 1
        sum = sum + i
        print(i)
print('Banyaknya bilangan ganjil : ' + str(a))
print('Jumlah seluruh bilangan   : ' + str(sum))
