a = int(input())
num_list = [(10, 20, 30), (1, 2), (5, 10, 15, 45)]
print([t[:-1] + (a,) for t in num_list])
