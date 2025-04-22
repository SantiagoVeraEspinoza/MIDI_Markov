import numpy as np
import math
from datetime import datetime

a = 25214903917
c = 11
m = 2**48 - 1

now = datetime.now()
X_N = int(now.strftime('%Y%m%d%H%M%S') + f"{now.microsecond:06d}")

min_x = float('inf')
max_x = float('-inf')


def rand(low, high):
    global X_N
    x = (a * X_N + c) % m

    X_N = (x - low) / (high - low)

    return (X_N % (high-low)) + low

def rand_normal():
    global X_N

    return math.trunc((rand(0, 100) / 100) * 10000) / 10000