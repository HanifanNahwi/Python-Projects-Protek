def bmi(BB,TB):
    global rbmi
    rbmi = BB/(TB**2/10000)
    
print('===========Body Mass Index (BMI)===========')
a = float(input('Masukkan Berat Badan(Kg) anda  : '))
b = float(input('Masukkan Tinggi Badan(cm) anda : '))
bmi(a,b)

print('')

if(rbmi < 18):
    print('Status Anda : Kurus')
elif(18 <= rbmi < 23):
    print('Status Anda : Ideal')
elif(23 <= rbmi < 27):
    print('Status Anda : Gemuk')
elif(27 <= rbmi < 35):
    print('Status Anda : Obesitas')
elif(rbmi >= 35):
    print('Status Anda : Obesitas Morbid')
