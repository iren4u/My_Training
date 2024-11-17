toy = ['teddy' , 'fox' , 'dog' , 'cat']
print(toy)
print(toy[1])
toy[1] = "rabbit"
print(toy)
toy.append(True)
print(toy)
toy.extend(["shark" , 3])
print(toy)
toy.remove('dog')
print(toy)
print('cat'in toy)
print('teddy' not in toy)
