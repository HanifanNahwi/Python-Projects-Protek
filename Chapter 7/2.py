a = input('Masukkan nama file : ')

try:
    while True:
        file = open(a, 'a')
        b = input('Data yang mau ditambahkan : ')
        file.write(b)
        file.close
        n = input('Mau lagi? (y/n) :')
        if n != 'y':
            break
    file = open(a, 'r')
    print(file.read())
except ValueError:
    print('salah')
