from random import randint

def quicksort(arr):
    if len(arr) < 2:
        return arr
    mid = partition(arr)
    return quicksort(arr[:mid]) + [arr[mid]] + quicksort(arr[mid+1:])

def partition(lst):
    pivot_id = randint(0, len(lst)-1)
    pivot = lst[pivot_id]
    j = 0
    lst[0], lst[pivot_id] = lst[pivot_id], lst[0]
    for i in range(1, len(lst)):
        if lst[i] <= pivot:
            j += 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[0], lst[j] = lst[j], lst[0]
    return j


if __name__ == '__main__':
    print('Введите целые числа, для которых вы хотите выполнить сортировку.\nЧисла необходимо разделять пробелами. Пример: 7 15 0 9')
    nums_list = [int(i) for i in input().split()]
    print(quicksort(nums_list))
   