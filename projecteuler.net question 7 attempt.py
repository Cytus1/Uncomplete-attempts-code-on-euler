factor_list = []
prime_list = []
sort_list = []

def find_factors(value):
    if value % 2 != 0:
        for check_factor in range(1, value + 1):
            if value % check_factor == 0:
                factor_list.append(check_factor)


def is_prime(value):
    for number in range(2, value):
        if value % number == 0:
            return False
    return True

i = 1
prime_number_count = 0
while prime_number_count < 10001:
    find_factors(i)
    i += 1

    for items in factor_list:
        if is_prime(items):
            prime_list.append(items)


    for items in prime_list:
        if items not in sort_list:
            sort_list.append(items)
            prime_number_count += 1
            
    print(prime_number_count)

print(sort_list)
