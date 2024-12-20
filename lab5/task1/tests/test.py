import time
import unittest
from lab5.utils import read_data, write_data, generations
import tracemalloc
from lab5.task1.src.task1 import check_heap

generations("heap", 5, 0,"C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab5/task1/txtf/input.txt")

def print_time_memory(func):
    n, data = read_data("C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab5/task1/txtf/input.txt", 1)

    tracemalloc.start()
    start_time = time.time()

    func(data)

    print("memory usage task 1: ", tracemalloc.get_traced_memory()[1] / 2**20, "Mb")
    print("--- %s seconds ---" % (time.time() - start_time))
    memory = tracemalloc.get_traced_memory()[1] / 2**20
    times = time.time() - start_time

    tracemalloc.stop()

    write_data(func(data), "C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab5/task1/txtf/output.txt")
    print(n, data)
    print(func(data))
    print("\n")
    return memory, times


class TestTask(unittest.TestCase):

    def test_should_check_time_memori_max_value(self):
        expected_memory = 256
        expected_time = 2
        m, t = print_time_memory(check_heap)

        self.assertLessEqual(t, expected_time, f"Значение {t} превышает порог {expected_time}")
        self.assertLessEqual(m, expected_memory, f"Значение {m} превышает порог {expected_memory}")

    def test_correct_work(self):
        self.assertEqual(check_heap([1, 0, 1, 2, 0]), "NO")
        self.assertEqual(check_heap([5, 3, 4, 2, 1]), "NO")
        self.assertEqual(check_heap([7, 8, 9, 10, 11, 12, 13]), "YES")
        self.assertEqual(check_heap([10, 1, 2, 5, 6, 3, 4]), "NO")
        self.assertEqual(check_heap([20, 15, 18, 10, 12, 14, 16]), "NO")
        self.assertEqual(check_heap([1, 3, 2, 5, 4]), "YES")
        self.assertEqual(check_heap([1, 4, 9, 16, 25, 36, 49]), "YES")


