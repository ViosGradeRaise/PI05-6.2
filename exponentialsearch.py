def binary_search(arr, left, right, target):
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def exponential_search(arr, target):
    n = len(arr)

    # 1. Проверяем первый элемент
    if arr[0] == target:
        return 0

    # 2. Экспоненциально увеличиваем границу диапазона
    bound = 1
    while bound < n and arr[bound] < target:
        bound *= 2

    # 3. Выполняем бинарный поиск в найденном диапазоне
    left = bound // 2
    right = min(bound, n - 1)

    return binary_search(arr, left, right, target)
    
data = [2,4,5,23,34,78,90,126]
print("Ищем 34:", exponential_search(data, 34))  # 4
print("Ищем 7:", exponential_search(data, 7))    # -1
