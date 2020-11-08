def faktorial(n):
    if n <= 1:
        return 1
    else:
        return n * faktorial (n-1)

def C(a,b):
    hasil = faktorial(a)//(faktorial(b)*faktorial(a-b))
    print ('C(5,3)= ', hasil)

def P(a,b):
    hasil = faktorial(a)//faktorial(a-b)
    print ('P(10,7)= ', hasil)

a,b = 5,3
C(5,3)

a,b = 10,7
P(10,7)
