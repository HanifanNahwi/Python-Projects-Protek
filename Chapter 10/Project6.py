def enkripsi(x, y):
    x = x.upper()
    listeks = list(x)
    for i in range(len(listeks)):
        if(listeks[i] != ' '):
            if(ord(listeks[i]) + y < 91):
                asci = ord(listeks[i])
                enkrip = asci + y
                listeks[i] = chr(enkrip)
            else:
                asci = ord(listeks[i])
                enkrip = (asci + y) - 26
                listeks[i] = chr(enkrip)
        else:
            continue
    result = ''.join(listeks)
    return result
try:
    print('----------------------_Program Caesar_----------------------\n')
    print('Note : Pastikan huruf anda sudah KAPITAL')
    a = input('Masukkan letak dan nama file : ')
    file = open(a, 'r')
    c = file.read()
    key = int(input('keyword : '))
    hasil = enkripsi(c, key)
    
    aa = open('d:enkripsi.txt', 'a')
    aa.write(hasil)
    aa.close()
    
    print('\nHasil pengenkripsian teks {0} adalah : {1}'.format(c, hasil))
except ValueError:
    print('Masukkan bilangan bulat')
