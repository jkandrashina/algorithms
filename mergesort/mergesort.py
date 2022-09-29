from collections import deque
from typing import List

def merge(left_arr: List[int], right_arr: List[int]) -> List[int]:
    i, j = 0, 0
    res = []
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            res.append(left_arr[i])
            i += 1
        else:
            res.append(right_arr[j])
            j += 1
    if i < len(left_arr):
        res.extend(left_arr[i:])
    elif j < len(right_arr):
        res.extend(right_arr[j:])
    return res

# 1. Рекурсивная версия сортировки слиянием
def recursive_mergesort(arr: List[int]) -> List[int]:
    assert len(arr) > 0
    if len(arr) < 2:
        return arr
    else:
        mid = len(arr) // 2
        left = recursive_mergesort(arr[:mid])
        right = recursive_mergesort(arr[mid:])
        return merge(left, right)


# 2. Итеративная версия сортировки слиянием
def iterative_mergesort(arr: List[int]) -> List[int]:
    assert len(arr) > 0
    q = deque()
    for i in range(len(arr)):
        q.append([arr[i]])
    while len(q) > 1:
        q.append(merge(q.popleft(), q.popleft()))
    return q.popleft()


if __name__ == '__main__':
    print('Введите числа, которые необходимо отсортировать.\nЧисла должны быть разделены пробелами. Пример: 1 2 6 11')
    user_input = input()
    lst = [int(i) for i in user_input.split()]

    print('Рекурсивная версия: ', recursive_mergesort(lst))
    print('Итеративная версия: ', iterative_mergesort(lst))