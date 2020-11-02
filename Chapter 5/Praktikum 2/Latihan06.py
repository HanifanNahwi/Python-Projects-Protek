print("Hai.. nama saya Mr. Lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silakan tebak ya!!!")
score = 100
from random import randint
bil = randint(0, 100)
  
n = int(input("Tebakan Anda : "))
while True:
    if (n < bil):
        print("Hehehe… Bilangan tebakan anda terlalu kecil")
        score = score - 2
        n = int(input("Tebakan Anda : "))
        if (score == 0):
            print("Kesempatan anda telah habis karena,")
            break
    elif (n > bil):
        print("Hehehe… Bilangan tebakan anda terlalu besar")
        score = score - 2
        n = int(input("Tebakan Anda : "))
        if (score == 0):
            print("Kesempatan anda telah habis karena,")
            break
    elif (n == bil):
        print("Yeeee… Bilangan tebakan anda BENAR :-)")
        break
print("Score Anda   : ", score)

