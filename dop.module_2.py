n = int(input('Введите число от 3 до 20: '))
result: str = ''
for i in range(1, 21):
    for j in range(i + 1, 21):
        if n % (i + j) == 0:
            result += str(i) + str(j)

print(result)
