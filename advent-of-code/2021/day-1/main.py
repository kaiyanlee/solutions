# Copyright (c) 2022 Kaiyan M. Lee
#
# The solutions are free software: you can redistribute them and/or modify
# them under the terms of the MIT license.

import os

f = open(os.path.join(os.path.dirname(__file__), "data.txt"), "r")

prev = -1
count = 0

while True:
    line = f.readline()

    if not line:
        break

    curr = int(line)

    if prev >= 0 and curr > prev:
        count += 1

    print("x:", prev, curr)

    prev = curr

f.close()

print(count)
