from typing import List

def insert(heap: List[int], el: int) -> None:
    heap.append(el)
    if len(heap) > 1:
        siftup(heap, len(heap) - 1)

def extractmax(heap: List[int]) -> int:
    heap[0], heap[-1] = heap[-1], heap[0]
    max_val = heap.pop(-1)
    if len(heap) > 1:
        siftdown(heap, 0)
    return max_val

def siftup(heap: List[int], i: int) -> None:
    while i > 0:
        parent = (i - 1) // 2
        if heap[parent] > heap[i]:
            break
        heap[i], heap[parent] = heap[parent], heap[i]
        i = parent
        
def siftdown(heap: List[int], i: int) -> None:
    while (i * 2) + 1 < len(heap):
        left = i * 2 + 1
        right = i * 2 + 2
        if right < len(heap) and heap[right] > heap[left]:
            largest = right
        else:
            largest = left
        if heap[i] > heap[largest]:
            break
        heap[i], heap[largest] = heap[largest], heap[i]
        i = largest

if __name__ == '__main__':
    k = int(input('Введите количество операций с кучей: '))
    
    print(f'''В следующих {k} строках введите название операции.\n
    Допустимые операции:
    1. insert x - вставка нового числа в кучу. Пример: insert 200.
    2. extractmax - извлечение максимального значения из кучи. Пример: extractmax.
    ''')
    
    ops = [input('Введите название операции: ').split() for i in range(k)]
    heap = []

    for op in ops:
        if op[0].lower() == 'insert':
            insert(heap, int(op[1]))
        elif op[0].lower() == 'extractmax' and heap:
            m = extractmax(heap)
            print(m)

    