def dataStat(x):
    #rata-rata
    data = len(x)
    jml = sum(x)
    a = jml/data
    #nilai tertinggi
    b = max(x)
    #nilai terendah
    c = min(x)
    dataStat = [a,b,c]
    print(dataStat)

r = [1,5,3,6,8,2]
dataStat(r)
