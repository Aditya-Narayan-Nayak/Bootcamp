def convert_to_key_value_pairs(keys_list, values_list):
    dict_a = {}
    number_of_key = len(keys_list)
    for i in range(number_of_key):
        key = keys_list[i]
        value = values_list[i]
        dict_a[key]= value
    return dict_a
    
    
student_name = input().split(",")
student_ids = input().split(",")

student_details = convert_to_key_value_pairs(student_name,student_ids)
student_details_items = student_details.items()
student_details= sorted(student_details_items)
for item in student_details:
    print(*item)
