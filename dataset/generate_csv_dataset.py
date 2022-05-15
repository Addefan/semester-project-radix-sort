"""
Генерация наборов данных (формат хранения - CSV)
"""
import argparse
from random import randint
from os.path import join, split
from os import makedirs

DEFAULT_DESCRIPTION = 'CSV dataset generator script'
DEFAULT_SAMPLES = 100
DEFAULT_BOUNDARY = 100


def parse_args():
    """
    Парсинг аргументов командной строки (CLI).
    :return интерфейс для работы с аргументами.

    Больше информации на https://docs.python.org/3.7/howto/argparse.html
    """
    parser = argparse.ArgumentParser(description=DEFAULT_DESCRIPTION)

    parser.add_argument('output',
                        type=str,
                        help='output CSV file, e.g. data/output.csv')

    parser.add_argument('--samples',
                        type=int,
                        default=DEFAULT_SAMPLES,
                        help=f'number of samples to generate (default: {DEFAULT_SAMPLES})')

    parser.add_argument('--sort',
                        type=str,
                        help='type of sorting for which numbers are generated - counting or radix')

    parser.add_argument('--boundary',
                        type=int,
                        default=DEFAULT_BOUNDARY,
                        help=f'if counting sort, then the interval of generated numbers is [0, boundary]'
                             f'if radix sort, then the interval of generated numbers is [boundary // 10, boundary)'
                             f'(default boundary: {DEFAULT_BOUNDARY}')

    return parser.parse_args()


def generate_datasets_for_counting_sort(boundary):
    """
    Генерация наборов данных для сортировки подсчётом
    :param boundary: int - диапазон чисел для генерации - [0; interval]
    """
    # Порядковый номер набора данных
    for dataset in range(1, 6):

        # Количество элементов в наборе данных
        for amount in (100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 250000, 500000, 750000, 1000000):

            # Приведение к двухсимвольному числу
            dataset = str(dataset)
            dataset = '0' + dataset if len(dataset) == 1 else dataset

            # Пути к файлу и к директории, в которой файл находится
            dir_path = join('data', 'counting_sort', dataset)
            file_path = join(dir_path, str(amount) + '.csv')

            # Создание директорий по пути к файлу, если они не существуют
            makedirs(dir_path, exist_ok=True)

            # Заполнение файла числами
            with open(file_path, 'w', encoding='utf-8') as file:
                for _ in range(amount - 1):
                    file.write(str(randint(0, boundary)) + '\n')
                file.write(str(randint(0, boundary)))


def generate_datasets_for_radix_sort(digit):
    """
    Генерация наборов данных для поразрядной сортировки
    :param digit: int - разрядность генерируемых чисел
    """
    # Порядковый номер набора данных
    for dataset in range(1, 6):

        # Количество элементов в наборе данных
        for amount in (100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 250000, 500000, 750000, 1000000):

            # Приведение к двухсимвольному числу
            dataset = str(dataset)
            dataset = '0' + dataset if len(dataset) == 1 else dataset

            # Пути к файлу и к директории, в которой файл находится
            dir_path = join('data', 'radix_sort', dataset)
            file_path = join(dir_path, str(amount) + '.csv')

            # Создание директорий по пути к файлу, если они не существуют
            makedirs(dir_path, exist_ok=True)

            # Заполнение файла числами
            with open(file_path, 'w', encoding='utf-8') as file:
                for _ in range(amount - 1):
                    file.write(str(randint(10 ** (digit - 1), 10 ** digit - 1)) + '\n')
                file.write(str(randint(10 ** (digit - 1), 10 ** digit - 1)))


if __name__ == '__main__':
    args = parse_args()

    # валидация аргументов
    if args.samples < 0:
        raise ValueError('Number of samples must be greater than 0.')

    if args.sort not in ('counting', 'radix'):
        raise ValueError('The type of sorting can only be counting or radix')

    if args.boundary < 0:
        raise ValueError('Boundary number must be greater than 0.')

    # Создание директорий по пути к файлу, если они не существуют
    makedirs(split(args.output)[0], exist_ok=True)

    # запись данных в файл
    with open(args.output, 'w', encoding='utf-8') as file:
        for i in range(args.samples - 1):
            if args.sort == 'counting':
                file.write(str(randint(0, args.boundary)) + '\n')
            elif args.sort == 'radix':
                file.write(str(randint(args.boundary // 10, args.boundary - 1)) + '\n')
        if args.sort == 'counting':
            file.write(str(randint(0, args.boundary)))
        elif args.sort == 'radix':
            file.write(str(randint(args.boundary // 10, args.boundary - 1)))

    # Раскомментируйте сточку ниже, чтобы сгенерировать
    # сразу все наборы данных для сортировки подсчётом
    # generate_datasets_for_counting_sort(boundary=1000)

    # Раскомментируйте сточку ниже, чтобы сгенерировать
    # сразу все наборы данных для поразрядной сортировки
    # generate_datasets_for_radix_sort(digit=1)
