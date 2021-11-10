def convert_str_into_int(str_num_list):
  new_list = []
  for item in str_num_list:
    num = int(item)
    new_list.append(num)
   return new_list
str_num_list = input().split(",")
print(convert_str_into_int(str_num_list))
