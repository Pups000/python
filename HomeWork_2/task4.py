
print_list = input(f'Ввод данных ').split()

for ind, el in enumerate(print_list):
    if el.__len__()>10:
        el = el[:10]
    print(ind, el)