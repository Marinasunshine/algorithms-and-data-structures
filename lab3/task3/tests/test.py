import time
import unittest
from lab3.utils import *
import tracemalloc
from lab3.task3.src.task3 import scarecrow_sort

generations("matreshka", 5, 3,"C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab3/task3/txtf/input.txt")

def print_time_memory(func):
    n, k, matr = read_data("C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab3/task3/txtf/input.txt")

    tracemalloc.start()
    start_time = time.time()

    print("memory usage task 3: ", tracemalloc.get_traced_memory()[1] / 2**20, "Mb")
    print("--- %s seconds ---" % (time.time() - start_time))
    print("\n")
    memory = tracemalloc.get_traced_memory()[1] / 2**20
    times = time.time() - start_time

    tracemalloc.stop()

    write_data(func(n, k, matr), "C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab3/task3/txtf/output.txt")

    return memory, times


class TestTask(unittest.TestCase):

    def test_should_check_time_memori_value(self):
        expected_memory = 256
        expected_time = 2
        m, t = print_time_memory(scarecrow_sort)

        self.assertLessEqual(t, expected_time, f"Значение {t} превышает порог {expected_time}")
        self.assertLessEqual(m, expected_memory, f"Значение {m} превышает порог {expected_memory}")

    def test_correct_work(self):
        self.assertEqual(scarecrow_sort(3, 2, [2, 1, 3]), "НЕТ")
        self.assertEqual(scarecrow_sort(5, 3, [1, 5, 3, 4, 1]), "ДА")
        self.assertEqual(scarecrow_sort(1, 1, [42]), "ДА")
        self.assertEqual(scarecrow_sort(4, 2, [1, 2, 3, 4]), "ДА")
        self.assertEqual(scarecrow_sort(5, 3, [7, 7, 7, 7, 7]), "ДА")
        self.assertEqual(scarecrow_sort(4, 1, [4, 3, 2, 1]), "ДА")