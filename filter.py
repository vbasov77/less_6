lst = ['дело', 'тело', 'одеяло','дело', 'тело', 'одеяло','дело', 'тело', 'одеяло']

# Без применения функции filter
def slicing(lst, str):    
    result = []
    for i in lst:
        if i == str:
            result.append(i)
    return result      

print(slicing(lst, 'дело'))

# С применением filter

result = list(filter(lambda x: x == 'тело', lst))

print (result)