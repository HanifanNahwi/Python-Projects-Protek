nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80}, 
 	   {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100}, 
	   {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

print('='*79,'\nNIM\tNAMA\t\tN.MID\t\tN.UAS\t\tN.AKHIR\t\tSTATUS\n-------------------------------------------------------------------------------')
a = 0
for i in nilai:
    print(nilai[a]['nim'],end="")
    x = len(nilai[a]['nama'])
    print(nilai[a]['nama'].rjust(5+x),end="")
    y = str(nilai[a]['mid'])
    print(y.rjust(21-x),end="")
    y = str(nilai[a]['uas'])
    print(y.rjust(16),end="")
    rumus = round((nilai[a]['mid'] + 2*nilai[a]['uas'])/3)
    y = str(rumus)
    print(y.rjust(18),end="")
    if (rumus >= 60):
        print('lulus'.rjust(15))
    a += 1

print('-'*79)
