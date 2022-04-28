"""
Реализация сортировки подсчета для неотрицательных чисел - [0; n]
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
    for index, element in enumerate(initial_array):
        output[count[element] - 1] = element
        count[element] -= 1

    return output


if __name__ == "__main__":
    array = [1, 4, 4, 2, 8, 5, 3]
    print(counting_sort(array))
