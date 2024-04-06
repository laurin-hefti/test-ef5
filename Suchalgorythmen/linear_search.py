#Linear Suchalgorythmus

#data
data_numbers = [3,5,7,4,47,4,21,11,4,55,7,55,3,221,11,4,5,64,5]
data_words = ["lakd", "iaser", "akfjd", "adfj", "alfj", "ldfjla"]

# sortieralgorythmus hier, nicht notwendig weil lineare suche

#linear search function with offset default 0
#offset = die ersten n elemente der liste werden nicht beachtet
def linear_search(data, element, offset = 0):

    #iterating over every element
    for i in range(offset, len(data)):

        #if element found returning index of element
        if data[i] == element:
            return i

    #if element not in list then return -1 as a error
    return -1

#tests
print(linear_search(data_numbers, 7,3))
print(linear_search(data_words, "iaadfafafasdfser"))