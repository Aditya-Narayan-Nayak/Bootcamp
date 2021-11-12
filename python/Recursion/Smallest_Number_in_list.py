#Write a program to print Smallest Number in List
n = []
lenght = len(a)
for i in a:
    n.append(int(i))
    m = sorted(n, reverse = False)
print(m[0])
