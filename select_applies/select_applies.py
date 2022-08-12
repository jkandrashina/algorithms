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
    applies_intervals = [tuple(map(int, input('Введите 2 числа (время начала и конца), разделенные пробелом: ').split())) for i in range(n)]
    print(select_applies(applies_intervals))

if __name__ == '__main__':
    main()