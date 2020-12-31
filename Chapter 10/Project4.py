text = open('d:/so/2.txt', 'r')
list0 = []
list1 = []
list2 = []
for i in text:
    a = i.split('|')
    list0.append(a[0])
    list1.append(a[1])
    list2.append(a[2].strip())

search = str(input('Masukkan NIM yang mau dicari : '))
if search in list0:
    b = list0.index(search)
    print('\nData Mahasiswa')
    print('NIM     : ',list0[b])
    print('Nama    : ',list1[b])
    print('Alamat  : ',list2[b])
else:
    print('data tidak ditemukan')
