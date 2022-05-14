"""
Реализация сортировки подсчетом по разряду для неотрицательных чисел - [0; n]
"""


def counting_sort(initial_array, position):
    """
    Функция, которая сортирует массив по одному разряду подсчётом
    :param initial_array: list - массив, который нужно отсортировать
    :param position: int - разряд числа, по которому нужно отсортировать массив
    :return: list - отсортированный по разряду массив
    """

    # Подсчет кол-ва одинаковых элементов в первоначальном массиве
    count = [0] * (max_digit(initial_array) + 1)
    for element in initial_array:
        count[element // (10 ** position) % 10] += 1

    # Теперь count содержит фактическую позицию элементов в выходном массиве
    for index in range(1, len(count)):
        count[index] += count[index - 1]

    # Сортируем initial_array
    output = [0] * len(initial_array)

    for element in initial_array[::-1]:
        output[count[element // (10 ** position) % 10] - 1] = element
        count[element // (10 ** position) % 10] -= 1

    return output


def max_digit(initial_array):
    """
    Функция, которая ищет максимальную цифру в массиве из чисел
    :param initial_array: list - массив чисел
    :return: int - максимальная цифра в массиве чисел
    """
    answer = 0
    for number in initial_array:
        for digit in map(int, str(number)):
            if digit > answer:
                answer = digit
    return answer
