"""
Контрольное тестирование поразрядной сортировки
"""
import argparse
from sys import path
from os.path import split, abspath
from os import curdir, makedirs
from time import perf_counter

path.append(abspath(curdir))
from src.radix_sort import radix_sort  # noqa: E402

DEFAULT_DESCRIPTION = 'Radix sort benchmark script'
DEFAULT_TRIALS = 10


def parse_args():
    """
    Парсинг аргументов командной строки (CLI).
    :return интерфейс для работы с аргументами.

    Больше информации на https://docs.python.org/3.7/howto/argparse.html
    """
    parser = argparse.ArgumentParser(description=DEFAULT_DESCRIPTION)

    parser.add_argument('input',
                        type=str,
                        help='input CSV file, e.g. dataset/data/radix_sort/01/100.csv')

    parser.add_argument('output',
                        type=str,
                        help='output CSV file, e.g. benchmark/metrics.txt')

    parser.add_argument('--trials',
                        type=int,
                        default=DEFAULT_TRIALS,
                        help=f'number of test trials (default: {DEFAULT_TRIALS})')

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    if args.trials < 0:
        raise ValueError('Number of trials must be greater than 0.')

    # Создание директорий по пути к файлу, если они не существуют
    makedirs(split(args.output)[0], exist_ok=True)

    with open(args.input, 'r', encoding='utf-8') as inp_file, \
            open(args.output, 'w', encoding='utf-8') as out_file:

        # Вытаскивание количества поданых элементов из названия файла
        amount = int(split(args.input)[1].split('.')[0])

        # Создание массива, который нужно отсортировать
        initial_array = []
        for _ in range(amount):
            initial_array.append(int(inp_file.readline()))

        # Количество прогонов на наборе данных
        for trial in range(args.trials):

            # Замер времени сортировки
            start_time = perf_counter()
            radix_sort(initial_array)
            finish_time = perf_counter()

            # Запись времени сортировки в файл
            sorting_time = finish_time - start_time
            out_file.write(str(sorting_time * 1000) + '\n')
