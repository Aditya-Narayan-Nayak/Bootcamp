n = int(input())

nums_list = []
for i in range(n):
    command = input().split()
    if command[0] == 'insert':
        index = int(command[1])
        value = int(command[2])
        nums_list.insert(index, value)
    elif command[0] == 'append':
        value = int(command[1])
        nums_list.append(value)
    elif command[0] == 'pop':
        nums_list.pop()
    elif command[0] == 'remove':
        value = int(command[1])
        nums_list.remove(value)
    elif command[0] == 'sort':
        nums_list.sort()
    elif command[0] == 'print':
        print(nums_list)
