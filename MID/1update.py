print('===========Body Mass Index (BMI)===========')
BB = int(input('Masukkan Berat Badan(Kg) anda  : '))
TB = int(input('Masukkan Tinggi Badan(cm) anda : '))
bmi = BB/(TB**2/10000)

if(bmi < 18):
    print('Anda Kurus')
elif(18 <= bmi < 23):
    print('Anda Ideal')
elif(23 <= bmi < 27):
    print('Anda Gemuk')
elif(27 <= bmi < 35):
    print('Anda Obesitas')
elif(bmi >= 35):
    print('Anda Obesitas Morbid')
