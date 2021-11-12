# Write a program to Exteract the number in given string and print sum, minimum and miximum of tose number
string = input()
b = list(string)
a = []
for i in b:
    if i.isdigit():
        a.append(int(i))
print(sum(a))
print(min(a))
print(max(a))
