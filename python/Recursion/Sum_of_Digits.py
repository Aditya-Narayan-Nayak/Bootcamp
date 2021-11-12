#Write a program to recursively compute the sum of all the sum of all the digits in the given number N.

def sum_of_the_digits(number):
    if number < 10:
        return number
    else:
        return (number % 10) + sum_of_the_digits(number // 10)

number = int(input())
result = sum_of_the_digits(number)
print(result)
ccc
