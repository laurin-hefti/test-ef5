import csv
import matplotlib.pyplot as plt

file = open("mydata.csv", encoding="UTF8")

csv_reader = csv.reader(file, delimiter= ";")

time = []

for i,line in enumerate(csv_reader,1):
    if i == 1:
        print(line[0])
    else:
        time.append(line[0])
print(time)
file.close()

plt.plot(time)
plt.show()
