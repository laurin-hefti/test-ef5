zahl = input("welche zahl möchten sie")
sys = input("welches system wollen sie")

zahl = int(zahl)
sys = int(sys)

liste = []
while zahl >= sys:
    rest = zahl%sys
    liste.append(rest)
    if zahl//sys == 0:
        break
    zahl = zahl//sys
print(liste)
    