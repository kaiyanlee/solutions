# Copyright (c) 2022 Kaiyan M. Lee
#
# The solutions are free software: you can redistribute them and/or modify
# them under the terms of the MIT license.

# Solution: 233168


def multiples(x, y):
    sum = 0

    for i in range(1000):
        if i % x == 0 or i % y == 0:
            sum += i

    return sum


print(multiples(3, 5))
