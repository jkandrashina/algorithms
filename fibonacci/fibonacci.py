# 1. Динамическое программирование назад (сверху вниз)
# Рекурсивная реализация.

def fibTD(n: int) -> int:
    if fib_cache[n] == -1:
        if n <= 1:
            fib_cache[n] = n
        else:
            fib_cache[n] = fibTD(n - 1) + fibTD(n - 2)
    return fib_cache[n]


# 2. Динамическое программирование вперед (снизу вверх).
# Итеративная реализация.

def fibBU(n: int) -> int:
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[n]


# 3. Улучшенный алгоритм программирования вперед.
# Уменьшает объем потребляемой памяти
def fibBUImproved(n: int) -> int:
    if n <= 1:
        return n
    prev, curr = 0, 1
    for i in range(n - 1):
        prev, curr = curr, prev + curr
    return curr

if __name__ == '__main__':
    fib_num = int(input('Введите номер числа Фибоначчи: '))
    fib_cache = [-1 for i in range(fib_num + 1)]

    print(f'fibTD({fib_num}):          {fibTD(fib_num)}')
    print(f'fibBU({fib_num}):          {fibBU(fib_num)}')
    print(f'fibBUImproved({fib_num}):  {fibBUImproved(fib_num)}')