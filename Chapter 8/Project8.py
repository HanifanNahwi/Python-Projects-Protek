def rata(buah):
    harga = list(buah.values())
    jumlah = sum(harga)
    banyak = len(harga)
    rata2 = jumlah/banyak
    return rata2

a = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
print(rata(a))
