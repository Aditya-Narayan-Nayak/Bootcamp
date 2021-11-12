num_set = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100}
lista = input().split()

for item in lista:
    num = int(item)
    num_set.discard(num)
num_list = list(num_set)
num_list.sort()
print(num_list)
