def get_unique_paris(int_list, pair_sum):
    stop_index = len(int_list) - 1
    unique_paris_set = set()
    for cur_index in range(stop_index):
        num_1 = int_list[cur_index]
        num_2 = pair_sum - num_1
        remaining_list = int_list[cur_index+1:]
        if num_2 in remaining_list:
            pair = (num_1, num_2)
            sorted_pair = tuple(sorted(pair))
            unique_paris_set.add(sorted_pair)
    return unique_paris_set
    
    
def convert_string_to_int(str_num_list):
    new_list = []
    for item in str_num_list:
        num = int(item)
        new_list.append(num)
    return new_list
    
    
str_num_list = input().split(",")
pair_sum = int(input())
int_list = convert_string_to_int(str_num_list)
unique_paris = get_unique_paris(int_list, pair_sum)
unique_paris = list(unique_paris)
unique_paris.sort()
for pair in unique_paris:
    print(pair)
