def pentagonal_numbers (n = "oops"):
    return int(n*(3*n-1)/2)

pentagonal_n_list = [num for num in range(1, 101)]
pentagonal_n_list = [pentagonal_numbers(i) for i in pentagonal_n_list]

pen_list_range = len(pentagonal_n_list) - 1

for index in range(pen_list_range):
    for scan_index in range(pen_list_range):
        add_diff = pentagonal_n_list[index] + pentagonal_n_list[scan_index]
        sub_diff = pentagonal_n_list[index] - pentagonal_n_list[scan_index]
        
        if add_diff in pentagonal_n_list:
            if sub_diff in pentagonal_n_list:
                print(pentagonal_n_list[index])
                exit()
                
