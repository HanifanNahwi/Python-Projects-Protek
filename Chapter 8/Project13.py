nilai = [{'nim' : 'A01', 'nama' : 'Amir', 'mid' : 50, 'uas' : 80},
        {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},       
        {'nim' : 'A03', 'nama' : 'Cici', 'mid' : 50, 'uas' : 50}, 
        {'nim' : 'A04', 'nama' : 'Dedi', 'mid' : 20, 'uas' : 30},
        {'nim' : 'A05', 'nama' : 'Fifi', 'mid' : 70, 'uas' : 40}]

def tertinggi(a):
    max = 0
    data = {}
    for b in a:
        uas = b.get("uas")
        mid = b.get("mid")
        hitung = (mid + 2*uas)/3
        if(hitung > max):
            max = hitung
            data["nim"] = b.get("nim")
            data["nama"] = b.get("nama")
    print("Nilai tertinggi draih oleh mahasiswa bernama ", data["nama"] ,"dengan NIM", data["nim"])
tertinggi(nilai)
