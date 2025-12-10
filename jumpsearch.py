import math

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))  # длина прыжка
    prev = 0

    # 1. Прыгаем вперёд блоками размера step
    while prev < n and arr[min(prev + step, n) - 1] < target:
        prev += step

    # 2. Определили блок — теперь линейный поиск внутри него
    for i in range(prev, min(prev + step, n)):
        if arr[i] == target:
            return i

    return -1 # если элемент не встречается в списке

data = [2,4,6,23,24,45,67,78]
print("Ищем 23:", jump_search(data, 23)) # 3
print("Ищем 7:", jump_search(data, 7)) # -1
