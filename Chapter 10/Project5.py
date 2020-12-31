text = open('d:/so/5.txt', 'r')
print(text.read())
text.close()

text = open('d:/so/5.txt', 'r')
a = open('d:/so/jumlah.txt', 'a+')
list1 = []
list2 = []
x = 0
a.write('\nHasil penjumlahan Bil. diatas adalah :\n')
for i in text:
    b = i.split('|')
    list1.append(b[0])
    list2.append(b[1].strip())
    jumlah = int(list1[x]) + int(list2[x])
    a.write(str(jumlah))
    a.write('\n')
    x += 1
a.write('\n')
text.close()
a.close()

a = open('d:/so/jumlah.txt', 'r')
print(a.read())
a.close()
