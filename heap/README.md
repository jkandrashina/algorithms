# Операции с бинарной кучей

В модуле heap.py реализованы базовые операции для работы с max-кучей:

- добавление числа в кучу;
- извлечение максимума;
- просеивание вверх (после добавления числа в кучу);
- просеивание вниз (после извлечения максимального числа из кучи).


## Входные и выходные данные

**Вход:** Первая строка входа содержит число операций (k). Каждая из последующих k строк задает операцию одного из следующих двух типов:

- insert x , где x - целое число;
- extractmax.

Первая операция добавляет число **x** в кучу, вторая — извлекает максимальное число и выводит его.

**Выход:** набор максимальных чисел, полученных в результате выполнения операций extractmax.