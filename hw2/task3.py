dic = {'зима':[12,1,2],
       'весна':[3,4,5],
       'лето':[6,7,8],
       'осень':[9,10,11]
        }
mounth_number = int(input(f'Введите номер месяца '))

for mounth in dic:
        for el in dic[mounth]:
            if el == mounth_number:
                print(mounth)