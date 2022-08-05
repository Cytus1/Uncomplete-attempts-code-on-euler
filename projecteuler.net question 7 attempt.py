#   define prime
import math
prime_list = []
not_prime_list = []


def find_prime(x):
    if x == 2:
        prime_list.append(x)

    range_for_divisor = math.floor(math.sqrt(x))
    for check_factor in range(3, range_for_divisor + 1):
        if x % check_factor == 0:
            not_prime_list.append(check_factor)
        if x % check_factor != 0:
            prime_list.append(check_factor)


find_prime(1000)
print(not_prime_list)
print(prime_list)
