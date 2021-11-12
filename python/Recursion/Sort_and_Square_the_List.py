#Write a program to Sort and Square the List
list_a = input().split(',')
a = []
for i in list_a:
    a.append(int(i)**2)
print(sorted(a))
