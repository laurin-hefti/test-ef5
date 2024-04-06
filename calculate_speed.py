data_size = input("data size\n")
transaction_speed = input("transaction speed in bits/s\n")

def convert_to_bits(input):
    input = input.split(" ")
    size = int(input[0])
    mult = 1
    if "KB" in input[1]:
        mult = 1000
    elif "MB" in input[1]:
        mult = 1000**2
    elif "GB" in input[1]:
        mult = 1000**3
    elif "TB" in input[1]:
        mult = 1000**4
    else:
        mult = 1
    return size*mult

data_size_n = convert_to_bits(data_size)
t_s_n = convert_to_bits(transaction_speed)
print (data_size_n)
print(t_s_n)
print((data_size_n/t_s_n)*8)