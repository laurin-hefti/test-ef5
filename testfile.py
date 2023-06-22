file = open("test.txt", "r")
file_lines = file.readlines()
file.close()

key_words =  ["ABSORPTION" , "SPECTRUM", "TRANSITION", "ELECTRIC", "DIPOLE", "MOMNETS"]
offset = 5
imp_data = [0,1,2]
prop = [2,1]

def finde_linie(file_lines, key_words): 
    line = 0

    index = 0
    for i in file_lines:
        word = i.split(" ")
        count = 0
        for j in key_words:
            if j in word:
                count += 1
            else: break
        if count+1 == len(key_words):
            line = index
        index += 1
    
    return line

def collect_data(offset, linie, file):
    data = []

    for i in range(len(file)):
        if file[i + offset + linie] != "\n":
            pass
        else:
            break
        data.append(file[i + offset + linie])

    return data

def process_data(data, imp_data): #importend data
    processed_data = [[] for _ in range(len(data))]

    index = 0
    for i in data:
        d = i.split(" ")
        dd = []
        for j in d: 
            if j != "":
                dd.append(j)
        d = dd
        for j in imp_data:
            processed_data[index].append(d[j])
        index += 1
    
    return processed_data

def aver_fuc(data, prop):
    summ = 0
    a = 0 #average

    for i in data:
        summ += float(i[prop[0]])*float(i[prop[1]])
        a += float(i[prop[1]])

    return summ/a

def get_data(file_lines, key_words, offset, imp_data, func, prop):
    line = finde_linie(file_lines, key_words)

    data = collect_data(offset, line, file_lines)

    proc_data = process_data(data, imp_data)

    res_data = func(proc_data, prop)

    return res_data

value = get_data(file_lines, key_words, offset, imp_data, aver_fuc, prop)
print(value)