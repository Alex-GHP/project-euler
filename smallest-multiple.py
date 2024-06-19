#  2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder 

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import math

def smallest_multiple(n):
  lcm_value = 1
  for i in range(2, n + 1):
    gcd_value = math.gcd(lcm_value, i) 
    lcm_value = (lcm_value * i) // gcd_value 
  return lcm_value

print(smallest_multiple(20))