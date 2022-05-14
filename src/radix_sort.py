"""
Реализация поразрядной сортировки
"""
from counting_sort import counting_sort


def radix_sort(initial_array):
    """
    Функция, которая сортирует массив поразрядной сортировкой
    :param initial_array: list - массив, который нужно отсортировать
    :return: list - отсортированный массив
    """
    max_number = max(initial_array)
    for position in range(len(str(max_number))):
        initial_array = counting_sort(initial_array, position)
    return initial_array
