import time
import matplotlib.pyplot as plt

d1 = []
d2 = []

for k in range(100):
    time1 = []
    time2 = []
    for j in range(80):
        
        liste = []
        timestart = time.time()
        for i in range(1000*j):
            liste.append(1)
        liste.reverse()
        timeend = time.time()
        #print (timeend-timestart)
        time1.append(timeend-timestart)

        #liste = []
        #timestart = time.time()
        #for i in range(1000*j):
            #liste.insert(0,1)
        #timeend = time.time()
        #print (timeend-timestart)
        #time2.append(timeend-timestart)
    d1.append(time1)
    d2.append(time2)
    print(k)


def getsummlist(list):
    liste = [0 for _ in range(len(list[0]))]
    for i in range(len(list)):
        for j in range(len(list[i])):
            liste[j] += list[i][j]
    for i in range(len(liste)):
        liste[i] /= len(list)
    return liste

def getn(list):
    liste2 = []
    for i in range(len(list[0])):
        liste = []
        for j in range(len(list)):
            liste.append(list[j][i])
        liste.sort()
        k = len(liste)//2
        liste2.append(liste[k])
    return liste2


a1 = getsummlist(d1)
a2 = getsummlist(d2)

av1 = getn(d1)
av2 = getn(d2)
    
plt.plot(a1,"", av1,"", a2,"", av2)
plt.show()