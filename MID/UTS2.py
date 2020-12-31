def hitungst(vo,a,t):
    global St

    i = 0
    while (i < t):
        i += 1
        St = (vo * i) + (a * i**2/2)
        print('t =', i, ', ', 'S(t) = ', St)

print('============================Menghitung Jarak Tempuh Mobil============================')
a = float(input('Masukkan Kecepatan Mula-mula Mobil (m/s) : '))
b = float(input('Masukkan Percepatan Mobil (m/s^2)        : '))
c = 10

print('')

print('Jarak yang sudah ditempuh mobil untuk setiap detiknya (mulai dari t=1 hingga t = 10)')

hitungst(a,b,c)
