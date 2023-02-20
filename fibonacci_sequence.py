from functools import lru_cache

@lru_cache(maxsize = 1000)
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input('Enter the nth term in which you seek it\'s value '))
print(fibonacci(n))
