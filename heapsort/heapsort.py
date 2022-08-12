def siftdown(heap, i, size):
    while (i * 2) + 1 < size:
        left = i * 2 + 1
        right = i * 2 + 2
        if right < size and heap[right] > heap[left]:
            largest = right
        else:
            largest = left
        if heap[i] > heap[largest]:
            break
        heap[i], heap[largest] = heap[largest], heap[i]
        i = largest

def build_maxheap(arr):
    for i in range((len(arr) // 2) - 1, -1, -1):
        siftdown(arr, i, size=len(arr))

def heapsort(arr):
    build_maxheap(arr)
    size = len(arr) - 1
    for i in range(len(arr) - 1):
        arr[size], arr[0] = arr[0], arr[size]
        size -= 1
        siftdown(arr, 0, size)
    return arr


if __name__ == '__main__':
    arr = [int(i) for i in input().split()]
    print(heapsort(arr))
