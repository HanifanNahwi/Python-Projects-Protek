text = open('d:/so/2.txt', 'r')
line = text.readlines()
dict = {}
listD = []
for i in range(len(line)) :
    a = line[i].split('|')
    a[2] = a[2].replace('\n', '')
    dict = {'nim' : b[0], 'nama' : b[1], 'alamat' : b[2]}
    listD.append(dict)
print(listD)
