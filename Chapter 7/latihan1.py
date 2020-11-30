a = input('Masukkan nama file : ')
file = open(a, 'r')
print('isi file', a, ' adalah : ')
print(file.read())
