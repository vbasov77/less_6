x = 5
y = 3


# Обычный пример
def sum(x, y):
    n = x + y
    return n


print(sum(x, y))

# Пример с lambda
n = (lambda x, y: x + y)(x, y)

print(n)


# Обычный прмер

def hallo(name):
    print(f'Привет, {name}')


name = input('Введи своё имя ')

hallo(name)


# Пример с lambda

hallo_lambda = (lambda name: print(f'Вот тебе lambda, {name}'))(name)
print(hallo_lambda)