my_dict = {'Slava': 2022, 'Vova': 1992}
print(my_dict)
print(my_dict['Vova'])
print(my_dict.get('Charli'))
my_dict.update({'Polina': 1988, 'Mama': 1954})
print(my_dict)
a = my_dict.pop('Vova')
print(my_dict)
print(a)


my_set = {1, 2, 3, 1, 2, 3, 'Vova', 'Vova'}
print(my_set)
print(my_set.add(5))
print(my_set)
print(my_set.discard(1))
print(my_set)
