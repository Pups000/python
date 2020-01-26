fields_list = ['название', 'цена', 'количество', 'eд']
items_list = []
static_dict = {}

i = 1
while True:
    item = {}
    for el in fields_list:
        item.update({el: input(f'Введите {el} ')})
    items_list.append((i,item))
    if input(f'Прекратить ввод, нажмите n') == 'n':
        break
    i+=1

for el in fields_list:
    static_dict.update({el:[]})

for el in items_list:
    for field in fields_list:
        static_dict[field].append(el[1][field])

print(static_dict)