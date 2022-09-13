zahl = 10
liste = []
while zahl > 0:
    liste.append(zahl%2)
    zahl = zahl // 2
liste.reverse()
print (liste)