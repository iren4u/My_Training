def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print('---------------------')

print_params(2, False, 50)
print_params(4, 'string', 'none')
print_params(a = 'ten', b= 'eight')
print_params(b = True, c = 8)
print_params(a ='строка')
print_params(b = False)
print_params()

print('________________________')

values_list = [25, 72, 'string']
print_params(*values_list)
values_dict = {'a':5, 'b':'bottom', 'c':False}
print_params(**values_dict)
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)

print('_____________________________')

print_params(b = 25)
print_params(c=[1, 2, 3])



