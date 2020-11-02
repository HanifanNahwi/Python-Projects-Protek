#variabel
a = "Status Kelulusan :"
b = "Sebab            :"
print("Masukkan Nilai diantara 0 - 100")

#input nilai
indo = int(input("Bahasa Indonesia : "))
ipa = int(input ("IPA              : "))
mtk = int(input ("Matematika       : "))

#status kelulusan
if(indo > 100) or (indo < 0) or (ipa > 100) or (ipa < 0) or (mtk > 100) or (mtk < 0):
    print("Maaf, input ada yang tidak valid")
elif(indo >= 60 and ipa >= 60 and mtk >=70):
    print(a, "LULUS")
else:
    print(a, "TIDAK LULUS")
    
#sebab tidak lulus
if(indo < 60):
    print(b, "Nilai Bahasa Indonesia kurang dari 60")
elif(ipa < 60):
    print(b, "Nilai IPA kurang dari 60")
elif(mtk < 70):
    print(b, "Nilai Matematika kurang dari 60")
