"""Project Euler - Problem 4
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_palindrome(n: int) -> bool:
    for i in range(len(str(n))//2):
        if str(n)[i] != str(n)[len(str(n))-1-i]:
            return False
    return True

largest = 1
for i in range (999, 900, -1):
    for j in range(i, 900, -1):
        test = i*j
        if is_palindrome(test):
            if test > largest:
                largest = test
print(largest)