"""Игра угадай число"""

import numpy as np

number = np.random.randint(1, 101) # загадываем число

# количество попыток
count = 0

# узнаем десяток числа (0 = до 10, 10 = 100)
a = number // 10

# 
c = a * 10

while True:
    count += 1
    if number == 100:
        break
    elif a == 0:
        a += 1
        if a == number:
            break
    else:
        if c == number:
            break
        else:
            c += 1
            if c == number:
                break

print(f'Компьютер угадал число {number} за {count} количество попыток')