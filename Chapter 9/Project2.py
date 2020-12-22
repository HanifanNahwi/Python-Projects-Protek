try:
    n = int(input("Berapa tingkat = "))
except ValueError:
    print('Harus berupa angka')
    exit()
def bintang(n):
    if n > 0 :
        for i in range(n):
            a = "*" + "**"*i
            print(a.center(10," "))
    else:
        print("Angkamu negatif")
bintang(n)
