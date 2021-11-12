def remove_items(test_list, item):
	res = [i for i in test_list if i != item]
	return res
test_list = [5, 10, 20, 35, 5, 50, 20, 100, 200, 10, 150, 100, 100]
item = int(input())
res = remove_items(test_list, item)
print (str(res))
