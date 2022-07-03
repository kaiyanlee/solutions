# Copyright (c) 2022 Kaiyan M. Lee
#
# The solutions are free software: you can redistribute them and/or modify
# them under the terms of the MIT license.

# Solution: 4613732


def sum_fib(l1, l2, sum, max):
    l3 = l1 + l2

    if l3 >= max:
        return sum + 2
    elif l3 <= 2:
        return 0
    else:
        if l3 % 2 == 0:
            sum += l3

        return sum_fib(l2, l3, sum, max)


print(sum_fib(1, 2, 0, 4000000))
