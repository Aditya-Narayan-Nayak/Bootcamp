n = int(input())

multiplies_of_2 = set()
multiplies_of_3 = set()

for i in range(1, n+1):
    multiplies_of_2.add(2*i)
    multiplies_of_3.add(3*i)
    
diff = multiplies_of_2.difference(multiplies_of_3)
symantric_diff = multiplies_of_2.symmetric_difference(multiplies_of_3)

diff = list(diff)
symantric_diff = list(symantric_diff)

diff.sort()
symantric_diff.sort()

print(diff)
print(symantric_diff)

