import math

AB = 125
kecepatan1 = 62

BC = 256
kecepatan2 = 70

jam = 6
menitAB = math.ceil(AB / kecepatan1*60)#121
menitBC = math.ceil(BC / kecepatan2*60)#220
menitistirahat = 45
totalmenit = menitAB + menitBC + menitistirahat#386
totaljam = (totalmenit//60)+jam
totalmenit2 = totalmenit%60
print(totaljam)
print("Jika Pak Amir berangkat pukul 06.00 dan sempat istirahat 45 menit di kota B, maka")
print("Pak Amir akan sampai di kota C pukul", (totaljam),".",(totalmenit2))
