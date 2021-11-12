# Write a program to print Difference Between Max and Min in the list
k=input().split(",")
n=[]
for i in k:
    n.append(int(i))
    m=sorted(n , reverse=True)
u = (m[0])

for i in k:
    n.append(int(i))
    b=sorted(n , reverse=False)
v = (b[0])

print(u - v) 
