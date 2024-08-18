def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        flag = True
        for i in range(2, result):
            if result % i == 0:
                print('Составное')
                flag = False
                break
        if flag:
            print('Простое')
        return result
    return wrapper

@is_prime
def sum_three(*args):
    return sum(args)

result = sum_three(2, 3, 6)
print(result)