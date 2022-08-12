# 1. Рекурсивная реализация алгоритма Евклида
def recursive_gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a >= b:
        return recursive_gcd(a % b, b)
    if a < b:
        return recursive_gcd(a, b % a)


# 2. Итеративная реализация алгоритма Евклида
def iterative_gcd(a, b):
    while a and b:
        if a >= b:
            a = a % b
        else:
            b = b % a
    return max(a, b)


if __name__ == '__main__':
    print('Введите 2 целых числа, разделенных пробелами.\nТолько одно из чисел может быть равным нулю, но не оба одновременно:')
    a, b = tuple(int(i) for i in input().split())
    
    print('Рекурсивная версия: ', recursive_gcd(a, b))
    print('Итеративная версия: ', iterative_gcd(a, b))