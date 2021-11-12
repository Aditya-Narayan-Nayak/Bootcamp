# Write a program to  recursively compute the value of A rasied to the power B.
def calculate_power(x, y):
    if y == 1:
        return x
    else:
        y -= 1
        return x * calculate_power(x, y)


a = int(input())
b = int(input())
print(calculate_power(a, b))
