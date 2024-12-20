# Задание №7 по варианту  : `Максимум в движущейся последовательности`
Студентка ИТМО,  Заботкина Марина Александровна 465908

## Вариант 7

## Задание 
Задан массив из n целых чисел - a1, ..., an и число m < n, нужно найти максимум среди последовательности ("окна") {ai, ..., ai+m−1} для каждого значения
1 ≤ i ≤ n − m + 1. Простой алгоритм решения этой задачи за O(nm) сканирует каждое "окно"отдельно. Ваша цель - алгоритм за O(n).

## Input / Output 

![image](https://github.com/user-attachments/assets/a07420ea-8aee-43f9-b04e-974eb7bd8c22)

## Ограничения по времени и памяти

- Ограничение по времени. 5сек.
- Ограничение по памяти. 512мб.

## Запуск проекта
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/Marinasunshine/algorithms-and-data-structures.git
   ```
2. Перейдите в папку с проектом:
   ```bash
   cd algorithms-and-data-structures/lab4
   ```
3. Запустите программу:
   ```bash
   python src/task7.py
   ```

4. Запуск тестов:
   ```bash
   python tests/test.py
   ```