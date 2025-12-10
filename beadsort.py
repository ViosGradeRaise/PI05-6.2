def bead_sort(arr):
    max_val = max(arr)

    # 1. Строим "решетку" из бусин
    grid = [[0] * max_val for _ in arr]

    # 2. Расставляем бусины (1 = есть бусина)
    for row_idx, value in enumerate(arr):
        for i in range(value):
            grid[row_idx][i] = 1

    # 3. Под действием "гравитации" бусины падают вниз
    for col in range(max_val):
        bead_count = 0
        # считаем, сколько бусин в столбце
        for row in range(len(arr)):
            bead_count += grid[row][col]
            grid[row][col] = 0

        # "опускаем" бусины вниз
        for row in range(len(arr) - bead_count, len(arr)):
            grid[row][col] = 1
    # 4. Считываем отсортированный массив
    result = [sum(row) for row in grid]
    return result

data = [3, 1, 2, 4, 3]
print('Исходный:',data)
print('Отсортированный:',bead_sort(data))

# не подходит для отрицательных чисел + неудобно работать с дробными числами (дополнительные расходы)
