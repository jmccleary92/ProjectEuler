"""Project Euler — Problem 3
Largest Prime Factor

The prime factors of 13195 are 5,7,13 and 29.

What is the largest prime factor of the number 600851475143?
"""

def solve() -> int:
    n = 600851475143
    factor = 2
    last_factor = 1

    while n > 1:
        if n % factor == 0:
            last_factor = factor
            n //= factor
            while n % factor == 0:
                n //= factor
        factor += 1 if factor == 2 else 2  # Increment by 1 if 2, else by 2 to check only odd numbers

    return last_factor


if __name__ == "__main__":
    print(solve())