n = int(input('введите количество элементов 1 списка: '))
m = int(input('введите количество элементов 2 списка: '))
list1 = []
list2 = []

print('введите элементы 1 списка')
for i in range(n):
    list1.append(int(input(f'{i}й: ')))
print('введите элементы 2 списка')
for i in range(m):
    list2.append(int(input(f'{i}й: ')))
    
result_set = set(list1).intersection(set(list2))
result = sorted(list(result_set))

print(result)