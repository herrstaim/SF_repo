"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    # Узнаем разряднось числа (0 - до 10, 10 - 100, от 1 до 9 - от 10 до 99)
    dig_number = number // 10
    # Если число от 10 до 99 - то с данного десятка начинается подбор числа
    dec_number = dig_number * 10

    while True:
        
        # Если число равно 100 - выход из цикла
        if dig_number == 10:
            count += 1
            dig_number *= 10
            if dig_number == number:
                break

        # Если число от 1 до 9
        elif dig_number == 0:
            count += 1
            dig_number += 1
            if dig_number == number:
                break

        # Проверка чисел в диапазоне от 10 до 99
        else:
            # Проверка десятков (10, 20, 30 и т.д.)
            count += 1
            if dec_number == number:
                break
            # Проверка чисел в диапазонах между десятками (11, 25, 98 и т.д.)
            else:
                count += 1
                dec_number += 1
                if dec_number == number:
                    break

    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    # загадали список чисел
    random_array = np.random.randint(1, 101, size=(1000))

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score

if __name__ == "__main__":
    # RUN
    score_game(random_predict)
