# The sum of the squares of the first ten natural numbers is 385

# The square of the sum of the first ten natural numbers is 3025

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 2640

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sum_square_difference(n):
    sum_squares = 0
    for i in range(1, n + 1):
        sum_squares += i ** 2
    sum = 0
    for i in range(1, n + 1):
        sum += i
    square_sum = sum ** 2
    return square_sum - sum_squares

print(sum_square_difference(100))