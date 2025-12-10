def bucket_sort(arr):
    # 1. Создаём несколько пустых корзин
    buckets = [[] for _ in range(len(arr))]

    # 2. Помещаем элементы в корзины согласно формуле распределения
    for num in arr:
        index = int(num * len(arr))  # предполагаем, что num ∈ [0,1)
        buckets[index].append(num)
  
    # 3. Сортируем каждую корзину отдельно
    for i in range(len(buckets)):
        buckets[i].sort()

    # 4. Объединяем содержимое корзин обратно в один массив
    result = []
    for bucket in buckets:
        result.extend(bucket)
    return result

data = [0.83, 0.02, 0.24, 0.57, 0.68, 0.74, 0.33, 0.41, 0.52, 0.91, 0.11, 0.18] # хорошие данные
sorted_data = bucket_sort(data)
print('Исходный:', data)
print('Отсортированный:', sorted_data)
