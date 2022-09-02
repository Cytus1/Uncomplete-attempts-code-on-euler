#   find factor, select prime, add to list, scan for 10001st prime

factor_list = []
prime_list = []


#   find factors
def find_factors(value):
    if value % 2 != 0:
        for check_factor in range(1, value + 1):
            if value % check_factor == 0:
                factor_list.append(check_factor)


#   detect prime, idea : the following then do len = 2
def is_prime(value):
    for number in range(2, value):
        if value % number == 0:
            return False
    return True


find_factors(99)

for items in factor_list:
    if is_prime(items):
        prime_list.append(items)
print(prime_list)
