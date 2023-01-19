smallest, largest = 2, 5

array = ([[a for b in range(smallest, largest + 1)]for a in range(smallest, largest + 1)])

for list in array:
    for place in range(2 - 2, 5 - 1):
        list[place] = (list[place]) ** (place + 2)
        
unique_scan_array = []

for list in array:
    for num in list:
        unique_scan_array.append(num)

print(f'element size of unique list for scan: {len(unique_scan_array)}')

combination_range = (largest - smallest + 1) ** 2

unique_array = []
for i in unique_scan_array:
    if i not in unique_array:
        unique_array.append(i)

print(f'Mininum: {smallest} Largest: {largest} Range: {combination_range}')
print(f'Distinct terms: {len(unique_array)}')

unique_array.sort()
print(unique_array)
