# Неточное сравнение строк
# https://habr.com/ru/post/671136/
import math


def jaro_distance(s1: str, s2: str) -> float:
    """Функция определения расстояния Джаро
    (неточное сравнение строк)
    s1, s2 - строки
    резултат - расстояние Джаро (0..1)
    0 - точное совпадение
    1 - полное несовпадение"""

    s1 = s1.lower()
    s2 = s2.lower()

    # Определяем количество точных совпадений
    e = 0
    for ch1, ch2 in zip(s1, s2):
        if ch1 == ch2:
            e += 1

    # Вычисляем длину совпадений
    l = math.floor(max(len(s1), len(s2)) / 2) - 1

    # Находим количество неполных совпадений
    # Поиск совпадений производится путем сравнения каждой буквы из первой строки
    # с подстрокой i +/- l второго слова (где i индекс буквы первого слова)
    z = 0
    for i, ch in zip(range(len(s1)), s1):
        # Определяем нижний и верхний допустимые индексы для подстроки
        l_bound = 0 if i - l < 0 else i - l
        u_bound = len(s2) if i + l > len(s2) else i + l
        # Выделяем подстроку
        s = s2[l_bound: i] + s2[i+1:u_bound+1]
        # Убираем средний символ подстроки
        # median_index = math.floor(len(s) / 2)
        # ss = s[0:median_index] + s[median_index+1:len(s)]
        # Ищием количество совпадений (неполных)
        z += s.count(ch)

    m = e + z
    t = z / 2

    if m == 0:
        d_j = 0
    else:
        l_1 = float(len(s1))
        l_2 = float(len(s2))
        d1 = float(m) / l_1
        d2 = float(m) / l_2
        d3 = float(m - t) / float(m)
        # d_j = (1 / 3.0) * (float(m) / l_1 + float(m) / l_2 + float(m - t) / float(m))
        d_j = (1/ 3.0) * (d1 + d2 + d3)

    return d_j

    return z


example_1 = "создание"
example_2 = "обедать"
example_3 = "кот"
print(jaro_distance(example_1, example_3))
