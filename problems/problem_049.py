"""
Problem 49 - Prime Permutations

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
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

def p(n: int) -> int | tuple[int, ...]:
    if n < 10:
        return n
    n_str = str(n)
    to_return = [n]
    for i in range(1, len(n_str)):
        to_return.append(int(n_str[i:] + n_str[0:i]))
    to_return = sorted(to_return)
    return tuple(to_return)

print(f"{p(213)}")