import random
import time
import matplotlib.pyplot as plt

def sort_list(liste, index):
    #sort list
    sort_list = [[] for _ in range(10)]

    for i in liste:
        
        #calculate the indext nummber of the nummber 
        nummer = (i%index)//int((index/10))

        #if the number is lower than the index it will be added to the corresponding store list in the sort_list, when not then added to the list with the index 0
        sort_list[nummer].append(i) if nummer < index else sort_list[0].append(i)

    #converts the multidimensional list to one list
    result_list = [i for sublist in sort_list for i in sublist]

    return result_list


def radix_sort(liste):
    #find how long the bigges number is
    maxlen = len(str(max(liste)))

    for i in range(maxlen):
        liste = sort_list(liste, 10**(i+1))
    
    return liste

#list with the times
times = []

for i in range(1,2):
    #generates a list with random numbers
    random_list = [random.randint(0,1000) for _ in range(i*100000000)]

    #starts the time
    start_time = time.time()

    #sort the list
    sorted_list = radix_sort(random_list)

    #ends the time
    end_time = time.time()

    #adds the time diverence to the time list
    times.append(end_time-start_time)

    print (end_time-start_time)

#shot the times
plt.plot(times)
plt.show()


