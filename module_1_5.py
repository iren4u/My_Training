immutable_var = (4, [5, 7], 'true', 'string')
print(immutable_var)
#immutable_var[0] = 3
#TypeError: 'tuple' object does not support item assignment
#кортеж неизменяем, но внутри он хранит изменяемые объекты
mutable_list = [4, [2, 9], 'false', 'string']
print(mutable_list)
mutable_list[0] = 8
mutable_list[2] = 'true'
print(mutable_list)