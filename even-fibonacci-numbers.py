# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with and , the first terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89...

# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

def even_fibonacci_numbers(limit=4000000):
    previous = 1
    current = 2
    sum = 0
    while current <= limit:
        if current % 2 == 0:
            sum += current
        previous, current = current, previous + current
    return sum

print(even_fibonacci_numbers())
