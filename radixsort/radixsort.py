import sys

def radixsort(arr, digits_in_num):
    for i in range(digits_in_num - 1, -1, -1):
        res = arr[:]
        digits = [0 for _ in range(10)]
        for item in arr:
            d = get_digit(item, i)
            digits[d] += 1
        for j in range(1, 10):
            digits[j] += digits[j - 1]
        for item in arr[::-1]:
            d = get_digit(item, i)
            res[digits[d] - 1] = item
            digits[d] -= 1
        arr = res
    return res


def get_digit(number, d_index):
    return int(str(number)[d_index])

def main():
    reader = (map(int, line.split()) for line in sys.stdin)
    nums = list(next(reader))
    reader.close()
    digits = len(str(nums[0]))
    print(radixsort(nums, digits))

if __name__ == '__main__':
    main()