# Copyright (c) 2022 Kaiyan M. Lee
#
# The solutions are free software: you can redistribute them and/or modify
# them under the terms of the MIT license.

# Solution: 6857


# Prime number is a whole number greater than 1 that can
# not be made by multiplying other whole numbers.
def is_prime(num):
    for n in range(2, int(num**0.5) + 1):
        if num % n == 0:
            return False

    return True


# Calculates the largest prime factor of a recursively.
def largest_prime_factor(a):
    b = 2

    while b < (a / 2 - 1):
        if is_prime(b) and a % b == 0:
            return largest_prime_factor(a / b)
        b += 1

    return int(a)


print(largest_prime_factor(600851475143))
