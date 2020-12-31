while True:
    try:
        text = open('d:/so/2.txt', 'a+')
        nim = input('Masukkan NIM      : ')
        nama = input('Masukkan Nama Mhs : ')
        almt = input('Masukkan Alamat   : ')
        
        a = nim + '|'
        text.write(a)
        b = nama + '|'
        text.write(b)
        text.write(almt+'\n')
        text.close
        
        ulangi = input('Ulangi input lagi? (y/n) : ')
        if ulangi == 'n':
            text = open('d:/so/2.txt', 'r')
            print('\nIsi file :')
            x = text.read()
            print(x)
            break
        elif ulangi == 'y' :
            continue
    except ValueError:
        print('input salah')
