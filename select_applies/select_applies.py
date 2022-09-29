def select_applies(applies):
    try:
        a = sorted(applies, key=lambda x: x[1])
        res = [a[0]]
    except IndexError:
        return []
    for i in range(1, len(a)):
        if a[i][0] >= res[-1][1]:
            res.append(a[i])
    return res

def main():
    n = int(input('Введите общее количество заявок: '))
    print(f'В следующих {n} строках введите 2 числа (начало временного интервала и его конец).\nПример: 10 12')
    applies_intervals = [tuple(map(int, input().split())) for i in range(n)]
    print(select_applies(applies_intervals))

if __name__ == '__main__':
    main()