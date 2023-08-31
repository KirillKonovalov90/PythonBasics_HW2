import random
n = int(input('введите количество кустов черники: '))
berry_bushes = []

for i in range(n):
    berry_bushes.append(random.randint(1, 9))
max_collected = berry_bushes[-1] + berry_bushes[0] + berry_bushes[1]

for i in range(1, len(berry_bushes) - 1):
    collected = (berry_bushes[i-1] + berry_bushes[i] + berry_bushes[i+1])
    if collected > max_collected:
        max_collected = collected

collected_last = berry_bushes[n-2] + berry_bushes[n-1] + berry_bushes[0]
if collected_last > max_collected:
    max_collected = collected_last

print(berry_bushes)
print(max_collected)

#краевые условия не знаю как обработать по другому, кроме как лапками вбивать,
#поэтому не совсем красиво получилось