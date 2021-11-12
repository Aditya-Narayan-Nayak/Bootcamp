# Write a program to print Kth Smallest Number in the list
k = int(input())

nums_list = numbers.split(",")
lenght_of_nums_list = len(nums_list)

for i in range(lenght_of_nums_list):
    nums_list[i] = int(nums_list[i])
    
nums_list = sorted(nums_list, reverse=True)
kth_largest_number = nums_list[-k]
print(kth_largest_number)
