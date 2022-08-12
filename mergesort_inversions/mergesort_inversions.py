def merge(left, right):
    res = []
    i, j = 0, 0
    count = 0
    while len(res) < len(left) + len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            count += len(left) - i
            j += 1
        if i == len(left) or j == len(right):
            res.extend(left[i:] or right[j:])
            break 
    return res, count

def mergesort(arr):
    if len(arr) < 2:
        return arr, 0
    else:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        left, count_left = mergesort(left)
        right, count_right = mergesort(right)
        merged, count_merged = merge(left, right)
    return merged, count_left + count_right + count_merged


if __name__ == '__main__':
    print('Введите массив, состоящий из целых чисел.\nЧисла должны быть отделены друг от друга пробелом. Пример: 2 3 9 2')
    array = [int(i) for i in input().split()]
    print('Количество инверсий в массиве: ', mergesort(array)[1])