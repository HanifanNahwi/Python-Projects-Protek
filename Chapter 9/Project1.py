def ubahuruf(kata, x, y):
    a = kata
    b = x
    c = y
    for i in range(len(c)):
        a = a.replace(b[i], c[i])
    print(a)

ubahuruf('MATEMATIKA', 'T', 'S')
