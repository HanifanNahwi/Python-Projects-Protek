nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80}, 
 	   {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100}, 
	   {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

print('=================================================\nNIM\tNAMA\t\tN.MID\t\tN.UAS\n-------------------------------------------------')
a = 0
for i in nilai:
    print(nilai[a]['nim'],end="")
    x = len(nilai[a]['nama'])
    print(nilai[a]['nama'].rjust(5+x),end="")
    y = str(nilai[a]['mid'])
    print(y.rjust(21-x),end="")
    y = str(nilai[a]['uas'])
    print(y.rjust(16))
    a += 1
print('-------------------------------------------------')
