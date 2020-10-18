import math

tarifsewa1 = 200000
tarifsewa2 = 10000

jammulai = 6
jamselesai = 23

menitmulai = 0
menitselesai = 50

lamasewa = math.floor((jamselesai - jammulai) + (menitselesai - menitmulai) / 60)
total = (lamasewa - 12) * tarifsewa2 + tarifsewa1
print("Total tarif = Rp.", total)
