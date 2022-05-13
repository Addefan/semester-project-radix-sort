"""
Реализация сортировки подсчетом для любых целых чисел - [-m; n]; m, n ∈ R; -m < n
"""


def counting_sort(initial_array):
    """return sorted array"""

    # Подсчет кол-ва одинаковых элементов в первоначальном массиве
    max_number, min_number = max(initial_array), min(initial_array)
    count = [0 for _ in range(min_number, max_number + 1)]
    for element in initial_array:
        count[element - min_number] += 1

    # Перезаписываем initial_array в отсортированном порядке
    initial_array = [number + min_number for number, repetitions in
                     enumerate(count) for _ in range(repetitions)]

    return initial_array
