def factorial_recursive(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

num = int(input("Enter a non-negative integer: "))
result = factorial_recursive(num)
print(f"The factorial of {num} is {result}.")
