data = """75 -1
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

#   append -1 on first row to extend static array; adjust for scaning index and prevent error

#   THIS SOLUTION IS A BIT OFF, IT GIVE 1064

two_dia_array = data.split("\n")
one_dia_array = []

for one_dia in range (0, len(two_dia_array)):
    num = two_dia_array[one_dia]
    num = num.split(" ")
    one_dia_array.append(num)

int_ver_one_dia_array = []
    
for row in one_dia_array:
    temp_array = []
    
    for str_num in row:
        str_num = int(str_num)
        temp_array.append(str_num)
    
    int_ver_one_dia_array.append(temp_array)
    
max_adjacent_number = []

adjacent_memory_left = 0
adjacent_memory_right = 1
equal = False

largest = 0

for row in int_ver_one_dia_array:
    
    if equal == True:
        pass
    
    """
    We don't need to scan for equal value in triangle for project euler 18, since
    this condition doesn't exist in this current problem.
    """
    
    if equal != True:
    
        if row[adjacent_memory_left] > row[adjacent_memory_right]:
            largest = row[adjacent_memory_left]
         
        if row[adjacent_memory_left] < row[adjacent_memory_right]:
            largest = row[adjacent_memory_right]
            
            adjacent_memory_right += 1
            adjacent_memory_left += 1
        
        if row[adjacent_memory_left] == row[adjacent_memory_right]:
            print("equal")
            equal == True
            
            largest == row[adjacent_memory_left]    #   left or right doesn't matter
            
        equal = False
    
    print(largest)
    
    max_adjacent_number.append(largest)

sum = 0
for num in max_adjacent_number:
    sum += num
    
print(sum)
