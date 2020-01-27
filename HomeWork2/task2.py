input_list = list(input())
print_list = list()
for el in range(1,len(input_list),2):
    print_list.append(input_list[el])
    print_list.append(input_list[el-1])
if len(print_list) != len(input_list):
    print_list.append(input_list[len(input_list) -1])
print(print_list)