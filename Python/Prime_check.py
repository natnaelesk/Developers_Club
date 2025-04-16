import math

def prime_check (n):
    if n < 2:
        return "Not Prime"

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return "Not Prime"

    return "Prime"

print(prime_check(43))