def mahal(buah):
    harga = list(buah.values())
    harga.sort(reverse=True)
    termahal = harga[0]
    for a, harga in buah.items():
         if harga == termahal:
              return a
a = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}

print('Buah yang harga satuannya paling mahal adalah', mahal(a))
