# переведём элементы списка в верхний регистр

lst = ['дело', 'тело', 'одеяло','дело', 'тело', 'одеяло','дело', 'тело', 'одеяло']

# без map()
lst_upper = []
for direction in lst:
    d = direction.upper()
    lst_upper.append(d)
print(f'Без map(): \n{lst_upper}')

# Используя map()
with_map = list(map(str.upper, lst))
print(f'Используя map(): \n{with_map}')