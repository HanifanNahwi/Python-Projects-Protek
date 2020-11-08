def sum(*all):
    a = 0
    for n in all:
        a += n
    print(a)

def average (*all):
    a = 0
    b = 0
    for n in all:
        a += n
        b += 1
    avg = a/b
    print(avg)

def max (*all):
    a = all[0]
    for n in all:
        if(n > a):
            a = n
    print(a)

def min(*all):
    a = all[0]
    for n in all:
        if(n < a):
            a = n
    print(a)
