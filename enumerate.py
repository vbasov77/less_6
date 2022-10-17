# Пронумеруем список

lst = [5, 3, 1, 0, 9, 7]

# Без enumerte()
i = 0
num = 1
en = []
while i < len(lst):
    en.append(str(num) + ', ' + str (lst[i]))
    i+=1
    num+=1
print (en)

# С применением enumerte()

enum_lst = list(enumerate(lst, 1))
print(enum_lst)

