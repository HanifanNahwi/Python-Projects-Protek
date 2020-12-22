mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO', 
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']

print('='*61,'\nNIM\tNAMA MAHASISWA\t\tTGL LAHIR\tTEMPAT LAHIR\n-------------------------------------------------------------')
a = 0
for i in mhs:
    split = i.split(":")
    print(split[0],end="")
    x = len(split[1])
    print(split[1].rjust(4+x),end="")
    z = split[2]
    y = z.replace("-","/")
    print(y.rjust(34-x),end='')
    x = len(split[3])
    print(split[3].rjust(6+x))

print('-'*61)
