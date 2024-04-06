#binary search

#data
data_numbers = [3,2,55,4,22,43,4,5533,5,223,553,2356,2,23,3,553,223,44,56]

#sortieralgorythmus notwendig weil binarysearch das voraussetzt
data_numbers.sort()

#prints the sorted array
print(data_numbers)

#binary search function
def binary_search(data, element):
    #set the current element to none
    current_element = None

    #set the index to the half length of the list as a startguess
    i = len(data)//2

    #set the count varibale to start with a step of a quarter of the list size
    count = 2

    #variable when just one step is taken then increment variable
    count_one_step = 0

    #while loop runs infinetly
    while True:
        
        #seting the current element to the guesst index of the element
        current_element = data[i]

        #if current_element is element break the rest of the loop must not be balled, thas why the condition is not set in the while condition
        if current_element == element:
            return i
        
        #if one step is taken twice then the element is not in list
        if count_one_step == 2:
            return -1

        #sets the step variable
        step = (len(data))//(2**count)

        #case if step is 0, set it to 1 to get forward in the searching process
        if step == 0:
            step = 1
            count_one_step += 1 

        if (current_element < element):
            #icrements the searching index by the step
            i += step

            #decrementing the searching index
        else:
            i -= step

        #if i bigger than listsize then element not in list, or if i smaler than 0, then the element is alsow not in list
        if (i >= len(data) or i < 0):
            return -1
        
        #icrements the count variable
        count += 1 

#tests
print(binary_search(data_numbers, 4))