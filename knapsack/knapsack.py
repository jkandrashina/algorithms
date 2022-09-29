from typing import List, Tuple

def knapsack(items_list: List[Tuple[int]], capacity: int) -> float:
    items = sorted(items_list, key=lambda x: -(x[0] / x[1]))
    total_cost = 0
    for cost, weight in items:
        if weight < capacity:
            total_cost += cost
            capacity -= weight
        else:
            total_cost += (cost / weight) * capacity
            break
    return f"{total_cost:.3f}"


if __name__ == '__main__':
    n = int(input('Введите количество имеющихся предметов: '))
    capacity = int(input('Укажите вместимость рюкзака: '))

    print(f'В следующих {n} строках введите стоимость и объем предмета в виде целых чисел, разделенных пробелами. Пример: 324 10')
    items_list = [tuple(map(int, input().split())) for i in range(n)]

    print('Максимальная стоимость предметов в рюкзаке: ', knapsack(items_list, capacity))