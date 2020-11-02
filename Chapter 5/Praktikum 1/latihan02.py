a = "Status Kelulusan :"
print("Masukkan Nilai diantara 0 - 100")
#input nilai
indo = int(input("Bahasa Indonesia : "))
ipa = int(input("IPA              : "))
mtk = int(input("Matematika       : "))

if(indo > 100) or (indo < 0) or (ipa > 100) or (ipa < 0) or (mtk > 100) or (mtk < 0):
    print("Maaf, input ada yang tidak valid")
elif(indo >= 60 and ipa >= 60 and mtk >=70):
    print(a, "LULUS")
else:
    print(a, "TIDAK LULUS")
