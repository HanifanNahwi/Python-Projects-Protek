def list1():
    file = open('d:/so/ch10.txt', 'r')
    lis = []
    for angka in file:
        lis.append(int(angka))
    return lis

text = open('d:/so/ch10.txt', 'r')
text = text.read()
print(text)

lis = list1()
x = 0
genap = 0
ganjil = 0
for i in lis:
    a = lis[x]
    if i % 2 == 0:
        genap += 1
    if i % 2 == 1:
        ganjil += 1
    x += 1

print('\n\nOutputnya:\nBanyaknya bilangan genap  : ', genap, '\nBanyaknya bilangan ganjil : ',ganjil)
