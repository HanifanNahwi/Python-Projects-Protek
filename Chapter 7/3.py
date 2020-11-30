print('------------------------------')
print('   PROGRAM HITUNG RATA-RATA
      ')
print('------------------------------')

sum = 0
bil = 0

while True:
    try:
        b = int(input('Masukkan Bilangan Bulat : '))
        sum += b
        bil += 1
        n = input('Mau lagi? (y/n) :')
        if n != 'y':
            break
    except ValueError:
        print('Bukan Bilangan Bulat')

print('Rata-ratanya adalah : ', sum/bil)
