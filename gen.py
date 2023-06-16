from random import randint
import time


def linear_congruent_method(size):
    """
    Линейный конгруэнтный метод [0, 16383]

    :param size: количество генерируемых чисел
    :type size: int

    :return: список псевдослучайных чисел
    :rtype: list
    """
    res = []
    M = (1 << 63) - 1

    k = 1 << 63
    b = int(time.perf_counter_ns() // 100)
    if b == M:
        b -= 1
    r0 = 13

    for i in range(size):
        r0 = (k * r0 + b) % M
        res.append(r0 % 16384)

    return res


def middle_products(size):
    """
    Метод серединных произведений [0, 16383]

    :param size: количество генерируемых чисел
    :type size: int

    :return: список псевдослучайных чисел
    :rtype: list
    """
    r0 = int(time.time()) % 128 + 1
    r1 = int(time.time()) % 128 + 1
    b = 11
    rez = []

    for i in range(size):
        r = (r0 * r1 * b) & 16383
        rez.append(r)
        r0 = r1
        r1 = r
        r0 += 13
        r1 += 17
        b += 2
    return rez


def std_randint(size):
    """
    Встроенный генератор псевдослучайных последовательностей [0, 16383]

    :param size: количество генерируемых чисел
    :type size: int

    :return: список псевдослучайных чисел
    :rtype: list
    """
    res = []
    for i in range(size):
        res.append(randint(0, 16384))
    return res
