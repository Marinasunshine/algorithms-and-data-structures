import time
import unittest
from lab2.utils import *
import tracemalloc
from lab2.task3.src.task3 import merge_sort

generations("random", 5, 0,"C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab2/task3/txtf/input.txt")

def print_time_memory(func):
    n, data = read_data("C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab2/task3/txtf/input.txt")

    tracemalloc.start()
    start_time = time.time()

    _, inversions = func(data)

    print("memory usage task 3: ", tracemalloc.get_traced_memory()[1] / 2**20, "Mb")
    print("--- %s seconds ---" % (time.time() - start_time))
    print("\n")
    memory = tracemalloc.get_traced_memory()[1] / 2**20
    times = time.time() - start_time

    tracemalloc.stop()

    write_data(inversions, "C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab2/task3/txtf/output.txt")
    result = read_data("C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab2/task3/txtf/output.txt")

    return memory, times, result


class TestTask(unittest.TestCase):

    def test_should_check_time_memori_value(self):
        n, data = read_data("C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab2/task3/txtf/input.txt")
        _, expected_result = merge_sort(data)
        expected_memory = 256
        expected_time = 2
        m, t, result = print_time_memory(merge_sort)

        self.assertEqual(result, expected_result)
        self.assertLessEqual(t, expected_time, f"Значение {t} превышает порог {expected_time}")
        self.assertLessEqual(m, expected_memory, f"Значение {m} превышает порог {expected_memory}")

    def test_correct_work(self):
        self.assertEqual(merge_sort([1, 8, 2, 1, 4, 7, 3, 2, 3, 6]), ([1, 1, 2, 2, 3, 3, 4, 6, 7, 8], 17))
        self.assertEqual(merge_sort([5, 4, 3, 2, 1]), ([1, 2, 3, 4, 5], 10))
        self.assertEqual(merge_sort([1, 2, 3, 4, 5]), ([1, 2, 3, 4, 5], 0))
        self.assertEqual(merge_sort([10, 9, 8, 7, 6, 5]), ([5, 6, 7, 8, 9, 10], 15))
        self.assertEqual(merge_sort([3, 1, 2]), ([1, 2, 3], 2))
