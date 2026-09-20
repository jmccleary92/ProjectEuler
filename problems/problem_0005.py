"""Project Euler - Problem 5
Smallest Multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def is_prime(n: int) -> bool:
    if n in (2, 3, 5):
            return True
    for i in (2, 3, 5):
        if n % i == 0:
            return False
    k = 1
    test = 5
    while test**2 <= n:
        for i in (1, 5):
            test = 6*k + i
            if n % test == 0:
                return False
        k += 1
    return True

# Powers of primes(pp): returns a dictionary of powers of primes that multiply to the number
# e.g. 20 = 2x2x5, so pp(20) = {2:2, 5:1}
def pp(n: int) -> dict[int, int]:
    toReturn = dict()
    if is_prime(n):
        toReturn = {n:1}
    else:
        i = 2
        while i <= n:
            while n % i == 0:
                if toReturn.get(i) is None:
                    toReturn[i] = 1
                else:
                    toReturn[i] += 1
                n //= i
            i += 1 if i == 2 else 2
    return toReturn

my_dict = dict()
for i in range(2, 21):
    d = pp(i)
    for key in d:
        if my_dict.get(key):
            my_dict[key] = max(my_dict[key], d[key])
        else:
            my_dict[key] = d[key]
num = 1
for i in my_dict:
    num *= i**my_dict[i]
print(num)