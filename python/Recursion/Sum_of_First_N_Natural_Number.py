#Write a program to recursively compute the sum of the number from 1 to N
def sum_of_numbers(n):
    if n == 1:  # Base case
        return 1
    else:
        return n + sum_of_numbers(n-1)  # Recursion


num = int(input())
result = sum_of_numbers(num)
print(result)
