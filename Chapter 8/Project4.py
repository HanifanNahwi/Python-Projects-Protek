sayur = ['bayam', 'kangkung', 'wortel', 'selada']

print('Daftar sayur anda', sayur)
print('\nMenu: \nA. Tambah data sayur \nB. Hapus data sayur \nC. Tampilkan data sayur')
a = str(input('Pilihan anda: '))

if a == 'A':
    tambah = str(input('Masukkan nama sayur :'))
    sayur.append(tambah)
    print('perubahan data sayur :', sayur)
elif a == 'B':
    try:
        hapus = str(input('Masukkan nama sayur :'))
        sayur.remove(hapus)
        print('perubahan data sayur :', sayur)
    except ValueError:
        print('Data yang anda masukkan tidak ada')
elif a == 'C':
    print('Daftar sayur anda', sayur)
else:
    print('Menu tidak ada')
    
