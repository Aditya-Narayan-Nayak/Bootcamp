# given an number n Write an program to print * in inverted way
n = int(input())
a = ""
k = n
for i in range(n):
    print("* " * (k - i))
