aruk = {"t1" : 15,
 "t2" : 25,
 "t3" : 11.2,
 "t4" : 99.3}

lista = ["t1", "t3"]
osszeg = 0

for termek in lista:
    osszeg += aruk[termek]
print(osszeg)
