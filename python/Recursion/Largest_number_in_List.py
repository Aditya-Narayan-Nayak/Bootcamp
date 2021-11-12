#Write a program to print the largest number in list
k=input().split(",")
n=[]
for i in k:
    n.append(int(i))
    m=sorted(n , reverse=True)
print(m[0])
