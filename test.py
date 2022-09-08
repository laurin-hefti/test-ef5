zahl = 16
summe = 0
list = []
maxl = 0
while (summe < zahl):
    z = 0
    while (2**z <= zahl-summe):
        z += 1
    z -= 1
    if (maxl == 0):
        maxl = z
    if (summe + 2**z <= zahl):
        list.append("1")
        summe += 2**z
    else:
        list.append("0")
while (len(list)<=maxl):
    list.append("0")
print (list)