import sys

def countsort(arr, max_digit):
    res = arr[:]
    digits = [0 for _ in range(max_digit + 1)]
    for item in arr:
        digits[item] += 1
    for i in range(1, max_digit + 1):
        digits[i] += digits[i - 1]
    for item in arr[::-1]:
        res[digits[item] - 1] = item
        digits[item] -= 1
    return res


if __name__ == '__main__':
    print('Введите целые числа, значения которых меньше или равны 10. Числа отделяются друг от друга пробелом.\nПример: 5 7 1 0 10 9')
    reader = (map(int, line.split()) for line in sys.stdin)
    nums = list(next(reader))
    reader.close()
    print(countsort(nums, max(nums)))