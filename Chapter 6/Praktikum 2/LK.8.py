def luasSegitiga(a, t):
    luas = a * t / 2
    return luas

print("Luas segitiga dengan alas ", 10,
      " dan tinggi ", 20,
      " adalah ", luasSegitiga(10, 20))
print("Luas segitiga dengan alas ", 15,
      " dan tinggi ", 45,
      " adalah ", luasSegitiga(15, 45))

total = luasSegitiga(10,20) + luasSegitiga(15, 45)
print("Luas total kedua segitiga tersebut adalah = ", str(total))
