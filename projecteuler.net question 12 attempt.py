import math


#   This solution ignores 1

class PROJECT_EULER_12:
    
    prime_factor = 0
    
    @staticmethod
    def triangle_formula(n):
        return int((n * (n + 1)) // 2)
    
    @staticmethod
    def is_prime(n):
        factor_list = []
        factor_list.append(n)
        for factor in range(1, (int(math.sqrt(n)) + 1)):
            if n % factor == 0:
                factor_list.append(factor)
                
            if len(factor_list) > 2:
                return False        
             
        if len(factor_list) == 2:
            return True
    
    #   calcuation & have interaction with class
    def prime_factorisation(value):
        
        print(f'The value is {value}')
        
        while value != 1:
            for check_factor in range(2, int(value) + 1):
                
                if value % check_factor == 0:
                    
                    if PROJECT_EULER_12.is_prime(check_factor) == True:
                        
                        print(f'{check_factor} is prime factor')
                        
                        PROJECT_EULER_12.add_prime_factor()
                        value = value // check_factor
                        
                        print(f'The value is {value}')
                        
                        break
                    
    @classmethod
    def add_prime_factor(cls):
        cls.prime_factor += 1
    
    @classmethod
    def reset_prime_factor(cls):
        cls.prime_factor = 0
        
    
if __name__ == "__main__":
                          
    i = 0
    while PROJECT_EULER_12.prime_factor < 1:
        
        PROJECT_EULER_12.reset_prime_factor()
        i += 1
        
        input = 7   # test
        
        triangle_numbers = PROJECT_EULER_12.triangle_formula(input)
        
        PROJECT_EULER_12.prime_factorisation(triangle_numbers)    

    print(f'The triangle number is {PROJECT_EULER_12.triangle_formula(input)}, with the prime factor of {PROJECT_EULER_12.prime_factor}')
