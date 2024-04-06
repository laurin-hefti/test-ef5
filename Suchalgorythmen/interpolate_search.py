#interpolate search

#data
data_numbers = [3,2,55,4,22,43,4,5533,5,223,553,2356,2,23,3,553,223,44]

#sortieralgorythmus notwendig weil binarysearch das voraussetzt
data_numbers.sort()

#prints the sorted array
print(data_numbers)

#interpolate search
def interpolate_search(data, element):
    
    #set current element
    current_element = None

    #lower border
    l = 0
    
    #upper border
    r = len(data)-1

    #set a count if it is to big then interrupt the search
    count = 0

    while True:

        #sets the estimated position
        p = int(l + (element - data[l])/(data[r]-data[l]) * (r-l))
        
        #sets the current element
        current_element = data[p]

        #if current_element = element return p
        if current_element == element:
            return p
        else:
            #if current element lower than element then increas the lower border
            if current_element < element:
                l = p + 1
            else:
                #if current element highter than element increas the upper border
                r = p - 1

        #if count to big then interrupt the search
        if count >= len(data):
            return -1
        
        count += 1
#tests
print(interpolate_search(data_numbers, 223))