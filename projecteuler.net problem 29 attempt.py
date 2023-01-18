array = ([[a for b in range(2, 5 + 1)]for a in range(2, 5 + 1)])
print(array)

for list in array:
    for place in range(2 - 2, 5 - 1):
        list[place] = (list[place]) ** (place + 2)

print(array)
