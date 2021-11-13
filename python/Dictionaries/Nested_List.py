def convert_str_into_int(str_num_list):
    new_list = []
    for item in str_num_list:
        num = int(item)
        new_list.append(num)
    return new_list
n = int(input())
num_list = []

for i in range(n):
    list_a = input().split()
    list_a = convert_str_into_int(list_a)
    num_list.append(list_a)
    
print(num_list)
