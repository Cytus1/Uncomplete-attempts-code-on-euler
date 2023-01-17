def fib(x):
    a = 0
    b = 1
    addition = 0
    while b < x:

        addition = a + b
        b = a
        a = addition
    
    return b

fib_list = [1, 1]
i = 1

while True:
    
    if fib(i) not in fib_list:
        fib_list.append(fib(i))
        
    if len(str(fib(i))) == 3:
        print(f'The first F.S to contain {len(str(fib(i)))} digit: {fib(i)}')
        break

    i += 1
    
