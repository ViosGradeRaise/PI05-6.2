def Pancake(arr):
    
    for i in range(len(arr), 0, -1):
        arr1 = arr[:i]
        a = max(arr1) # Находим максимальный элемент в подмассиве arr[:i]
        
        if arr1.index(a) != len(arr1) - 1:
            arr1 = arr1[arr1.index(a) ::-1] + arr1[arr1.index(a) + 1:] # Записываем подмассив до максимального элемента в обратном порядке
            arr[:i] = arr1[::-1] # Разворачиваем массив

    return arr

arr = [6, 2, 4, 1, 5, 8]
print("Исходный:", arr)
print("Отсортированный:", Pancake(arr))
