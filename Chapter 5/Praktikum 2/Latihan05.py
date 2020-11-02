print("Hai.. nama saya Mr. Lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silakan tebak ya!!!")
from random import randint
bil = randint(0, 100)
    
n = int(input("Tebakan Anda : "))
while True:
    if (n < bil):
        print("Hehehe… Bilangan tebakan anda terlalu kecil")
        n = int(input("Tebakan Anda : "))
    elif (n > bil):
        print("Hehehe… Bilangan tebakan anda terlalu besar")
        n = int(input("Tebakan Anda : "))
    elif (n == bil):
        print("Yeeee… Bilangan tebakan anda BENAR :-)")
        break
