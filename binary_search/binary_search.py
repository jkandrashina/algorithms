def binary_search(arr, key):
    left = 0
    right = len(arr) - 1
    while left <= right:
        middle = (left + right) // 2
        if arr[middle] == key:
            return middle
        elif arr[middle] > key:
            right = middle - 1
        else:
            left = middle + 1
    return -1

def main():
    print('Введите последовательность целых чисел, упорядоченных по неубыванию.\nПример: 1 5 7 7 8 9 10')
    nums = [int(num) for num in input().split()]

    print('Введите набор ключей в виде целых чисел.\nПример: 1 9 8 32')
    keys = [int(n) for n in input().split()]
    for key in keys:
        print(binary_search(nums, key), end=' ')

if __name__ == '__main__':
    main()