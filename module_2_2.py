print('Введите три целых числа ')
first = int(input('введите первое число '))
second = int(input('введите второе число '))
third = int(input('введите третье число '))
if first == second == third:
    print(3)
elif first == second or third == second or third == first:
    print(2)
else:
    print(0)