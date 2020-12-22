import math
try:
    n = int(input("Berapa tingkat = "))
except ValueError:
    print('Harus berupa angka')
    exit()
def bintang(n):
    if n > 0 :
        if (n%2 != 0):
            n = math.ceil(n/2)
            for i in range(n):
                a = "*" + "**"*i
                print(a.center(20,' '))
            xy = 0
            x = n-1
            for i in range(x):
                xy += 1
                a = '*' + '**'*(x-xy)
                print(a.center(20,' '))
        else:
            print("Harus Bilangan Ganjil")
bintang(n)
