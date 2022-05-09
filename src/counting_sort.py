"""
Реализация сортировки подсчетом для неотрицательных чисел - [0; n]
"""

def counting_sort(initial_array):
    """ return sorted array"""

    # Подсчет кол-ва одинаковых элементов в первоначальном массиве
    count = [0] * (max(initial_array) + 1)
    for element in initial_array:
        count[element] += 1

    # Теперь count содержит фактическую позицию элементов в выходном массиве.
    for index in range(1, len(count)):
        count[index] += count[index - 1]

    # Сортируем initial_array
    output = [0] * len(initial_array)
    for element in initial_array:
        output[count[element] - 1] = element
        count[element] -= 1

    return output
