n = int(input("Banyaknya Data: "))

data = []

for i in range(0, n):
    a = str(input("Masukkan data ke-%d: " % (i+1)))
    data.insert(1, a)

data.sort(reverse=True, key=len)
print(data)
