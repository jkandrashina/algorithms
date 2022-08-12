# 1. Для восстановления НВП используется дополнительный массив prev.
# В массив d заносится длина НВП для каждого элемента массива:
#   - d[i] - длина НВП, заканчивающейся в arr[i].
# В массив prev заносится индекс предыдущего элемента НВП или -1, если предыдущего элемента нет:
#   - prev = [-1, 0, -1] для arr = [5, 7, 1]
def lisBU(arr):
    d = []
    prev = []
    for i in range(len(arr)):
        d.append(1)
        prev.append(-1)
        for j in range(i):
            if arr[j] < arr[i] and d[j] + 1 > d[i]:
                d[i] = d[j] + 1
                prev[i] = j
    lis_len = 0
    k = -1
    for i in range(len(d)):
        if d[i] > lis_len:
            lis_len = d[i]
            k = i
    lis_items = [None] * lis_len
    j = lis_len - 1
    while k >= 0:
        lis_items[j] = arr[k]
        j -= 1
        k = prev[k]
    return lis_len, lis_items


# 2. Восстановление НВП без использования дополнительного массива
def lisBU_improved(arr):
    d = []
    for i in range(len(arr)):
        d.append(1)
        for j in range(i):
            if arr[j] < arr[i] and d[j] + 1 > d[i]:
                d[i] = d[j] + 1
    lis_len = 0
    k = -1
    for i in range(len(d)):
        if d[i] > lis_len:
            lis_len = d[i]
            k = i
    lis_items = []
    prev = float('inf')
    j = lis_len
    while j > 0:
        if d[k] == j and arr[k] < prev:
            lis_items.insert(0, arr[k])
            j -= 1
            prev = arr[k]
        k -= 1
    return lis_len, lis_items


if __name__ == '__main__':
    print('Введите последовательность целых чисел, разделенных пробелами.\nПример: 1 7 2 5')
    lst = [int(i) for i in input().split()]
    print('lisBU:          ', lisBU(lst))
    print('lisBU_improved: ', lisBU_improved(lst))