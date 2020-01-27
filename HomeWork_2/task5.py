my_list = [7, 5, 3, 3, 2]
user_number = int(input(f'Введите целое число '))

for ind, el in enumerate(my_list):
    if user_number > el:
        my_list.insert(ind,user_number)
        break
if my_list.__len__()-1 == ind:
    my_list.append(user_number)

print(my_list)