# Объеденим два списка

women = ["Татьяна", "Светлана", "Анна", "Марина"]
men = ["Сергей", "Александр", "Василий", "Николай"]

# Без zip()

i = 0
lst = []
while i < len(women):
    lst.append(women[i] + ', ' + men[i])
    i+=1   
    
print (lst)

# С применением zip()

zipped_list = list(zip(men, women))
print(zipped_list)