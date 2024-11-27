my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

r = len(my_list)

y = 0
while y < r:
    if my_list [y] == 0:
        y = y + 1
        continue
    elif my_list [y] > 0:
        print(my_list [y])
        y = y + 1
    elif my_list [y] < 0:
        break

