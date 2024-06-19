# projecteuler.net/problem=3

def largest_prime_factor(n):
    largest = float('-inf')
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0 and is_prime(i):
            if i > largest:
                largest = i
    return largest


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(largest_prime_factor(600851475143)) # 6857