import matplotlib.pyplot as plt

#get_sum  = lambda n,sum=0: (sum+int(i) for i in str(n))

def get_sum(n):
    n = str(n)
    sum = 0
    for i in n:
        sum += int(i)
    return sum

def isPirme(n):
    if n%2 == 0:
        return False
    if (get_sum(str(n))) % 3 == 0 and n != 3:
        return False
    i = 2
    while i < n//2:
        if n%i == 0:
            return False
        i += 1
    return True

points = []
number_prime = 0

for i in range(1,2000):
    j = 2;
    if isPirme(i):
        number_prime += 1
    while j < i:
        if isPirme(i) == False:
            break
        if isPirme(j):
            points.append(i*j)
        j+=1
    print(i)

points.sort()
print(len(points))
print(number_prime)
plt.plot(points)
plt.show()
        