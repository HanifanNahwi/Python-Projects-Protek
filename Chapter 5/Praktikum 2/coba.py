sum = 0
from random import randint
while True:
    bil = randint(0,10)
    print(bil)
    sum = sum + 1
    if bil == 5:
        break
print("Jumlah perulangan : " + str(sum))
