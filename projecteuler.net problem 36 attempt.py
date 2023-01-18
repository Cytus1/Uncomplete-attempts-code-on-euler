scan_num = 10
palindromic_bin_array = []

while scan_num < 1000000:

    convertor = str(bin(scan_num))
    convertor = convertor[2:]

    if convertor[0] != "0":
        reverse = convertor[::-1]
        if convertor == reverse:
            palindromic_bin_array.append(scan_num)
    
    scan_num += 1
    
    
sum = 0

for num in palindromic_bin_array:
    sum += num

print(sum)
