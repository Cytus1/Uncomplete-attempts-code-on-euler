#   give count on prime
import math
prime_number_count = 0
#   function to define prime


def find_factor(value):  # find factor
    factors = []
    for check_factor in range(1, int(math.sqrt(value)) + 1):
          if value % check_factor == 0:
              factors.append(check_factor)
              factors.append(value // check_factor)
          return factors


def is_prime(value):
    return len(find_factor(value)) == 2


factors_find = find_factor(prime_number_count)
largest_prime_factor = 0

while prime_number_count < 10001:
    
