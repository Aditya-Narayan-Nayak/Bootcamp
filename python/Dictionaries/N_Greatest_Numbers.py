list_a = [5, 20, 3, 7, 6, 8]
n = int(input())

list_a = sorted(list_a)
list_len = len(list_a)
res = list_a[list_len - n:]
for i in range(n):
    res[i] = str(res[i])
print(" ".join(res))
