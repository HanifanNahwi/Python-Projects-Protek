print("Masukkan Nilai diantara 0 - 100")
#input nilai
indo = int(input("Bahasa Indonesia : "))
ipa = int(input("IPA              : "))
mtk = int(input("Matematika       : "))

if(indo >= 60 and ipa >= 60 and mtk >=70):
    print("LULUS")
else:
    print("TIDAK LULUS")
