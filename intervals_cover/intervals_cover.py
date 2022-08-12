def intervals_cover(intervals):
    assert len(intervals) > 0

    a = sorted(intervals, key=lambda x: x[1])
    res = [a[0]]
    points = {a[0][1]}
    for i in range(1, len(a)):
        if a[i][0] > res[-1][1]:
            res.append(a[i])
            points.add(a[i][1])
    print(len(points))
    print(*points)


if __name__ == '__main__':
    n = int(input('Введите количество отрезков: '))
    
    print('Введите 2 числа (начало и конец отрезка) для каждого отрезка')
    intervals = [[int(border) for border in input(str(i + 1) + '-й отрезок: ').split()] for i in range(n)]
    
    intervals_cover(intervals)