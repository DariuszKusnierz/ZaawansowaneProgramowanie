def fusionPowerList(lista1:list, lista2:list) -> list:
    newList = []
    newList.extend(lista1)
    for element in lista2:
        if element not in newList:
            newList.append(element)
    
    newList = [element**3 for element in newList]
        
    return newList

lista1 = [2,5,81,6]
lista2 = [12,3,2,6,8]

print(fusionPowerList(lista1,lista2))
    