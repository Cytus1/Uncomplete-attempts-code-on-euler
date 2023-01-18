array = ([[a for b in range(2, 100 + 1)]for a in range(2, 100 + 1)])

for list in array:
    for place in range(2 - 2, 100 - 1):
        list[place] = (list[place]) ** (place + 2)
        
unique_total = 0
unique_scan_array = []

for list in array:
    for num in list:
        unique_scan_array.append(num)

print(f'element size of unique list for scan: {len(unique_scan_array)}')

for index in range(9801):
    count = 0
    for scan_index in range(9801):
        if unique_scan_array[index] == unique_scan_array[scan_index]:
            count += 1      
        if count > 1:
            break
    if count == 1:
        unique_total += 1
    
print(f'distinct terms: {unique_total}')
