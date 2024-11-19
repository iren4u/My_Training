#работа со словарем
my_dict = {'helen': 1988, 'Pasha': 1964, 'Luba': 1945}
print(my_dict)
print(my_dict['Luba'])
print(my_dict.get('Sveta'))
my_dict.update({'Rosa': 2005,
                'Petya': 1991})
print(my_dict)
print(my_dict.pop('Pasha'))
print(my_dict)

print()

#работа с множествами
my_set = {1, 1, 1, 'собака', 'list', 'list', 52.14, (2,3,4), (2,3,4)}
print(my_set)
my_set.add('кошка')
my_set.add('string')
print(my_set)
my_set.discard(52.14)
print(my_set)
