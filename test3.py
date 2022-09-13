import time
liste = []
timestart = time.time()
for i in range(10000):
    liste.append(1)
liste.reverse()
timeend = time.time()
print (timeend-timestart)

liste = []
timestart = time.time()
for i in range(10000):
    liste.insert(0,1)
timeend = time.time()
print (timeend-timestart)
