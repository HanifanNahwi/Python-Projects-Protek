import random

def shuffleString(x, n):
    text = list(x)
    listku = []
    for i in range(n):
        random.shuffle(text)
        a = (''.join(text))
        if a not in listku:
            listku.append(a)
    print(listku)

a = str(input('Masukkan kata = '))
b = int(input('Berapa Pengacakan = '))
shuffleString(a, b)
        
