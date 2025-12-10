def ternary_search(arr, left, right, target):
    if left > right:
        return -1

    # 1. Делим диапазон на три части
    third = (right - left) // 3
    mid1 = left + third
    mid2 = right - third

    # 2. Проверяем две ключевые точки
    if arr[mid1] == target:
        return mid1
    if arr[mid2] == target:
        return mid2

    # 3. Рекурсивно выбираем одну из трёх зон
    if target < arr[mid1]:
        return ternary_search(arr, left, mid1 - 1, target)
    elif target > arr[mid2]:
        return ternary_search(arr, mid2 + 1, right, target)
    else:
        return ternary_search(arr, mid1 + 1, mid2 - 1, target)

data = [3,5,7,11,16,25,33,67]
# left = индекс 0, right = индекс последнего элемента (len(data)-1)
print("Ищем 11:", ternary_search(data, 0, len(data)-1, 11)) # 3
print("Ищем 6:", ternary_search(data, 0, len(data)-1, 6)) # -1
