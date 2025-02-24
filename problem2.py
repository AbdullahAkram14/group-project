'''
File 2 (problem2.py): Write a function to calculate the factorial of a number.

Example:
Input: 5
Output: 120
'''
def calc_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *=i
        return result
    
n = 5
print(f"Factorial of {n} is : {calc_factorial(n)}")