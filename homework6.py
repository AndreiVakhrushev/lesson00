my_dict = {'Andrei': 1971, 'Diana': 1980, 'Ivan': 2020}
print(my_dict)
print(my_dict['Ivan'])
print(my_dict.get('Ivan'))
print(my_dict.get('Ilja'))
my_dict.update({'Ilja': 1994, 'Katja': 2001})
print(my_dict)
a = my_dict.pop('Andrei')
print(a)
print(my_dict)
print(my_dict.items())
my_set = {1, 2, 3, 4, 3, 2, 1, 36.6, 'Urban'}
print(my_set)
my_set.add(5)
my_set.add((1, 2, 3))
print(my_set)
my_set.remove('Urban')
print(my_set)