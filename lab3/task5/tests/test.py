import time
import unittest
from lab3.utils import *
import tracemalloc
from lab3.task5.src.task5 import h_index

generations("h", 100, 0, "C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab3/task5/txtf/input.txt")

def print_time_memory(func):
    data = read_data("C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab3/task5/txtf/input.txt")

    tracemalloc.start()
    start_time = time.time()

    print("memory usage task 5: ", tracemalloc.get_traced_memory()[1] / 2**20, "Mb")
    print("--- %s seconds ---" % (time.time() - start_time))
    print("\n")
    memory = tracemalloc.get_traced_memory()[1] / 2**20
    times = time.time() - start_time

    tracemalloc.stop()

    write_data(func(data), "C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab3/task5/txtf/output.txt")

    return memory, times


class TestTask(unittest.TestCase):

    def test_should_check_time_memori_value(self):
        expected_memory = 256
        expected_time = 2
        m, t = print_time_memory(h_index)

        self.assertLessEqual(t, expected_time, f"Значение {t} превышает порог {expected_time}")
        self.assertLessEqual(m, expected_memory, f"Значение {m} превышает порог {expected_memory}")

    def test_correct_work(self):
        self.assertEqual(h_index([3, 0, 6, 1, 5]), 3)
        self.assertEqual(h_index([5, 5, 5, 5]), 4)
        self.assertEqual(h_index([1, 3, 1]), 1)
        self.assertEqual(h_index([0, 0, 0]), 0)
        self.assertEqual(h_index([1000, 500, 200, 100, 50]), 5)
        self.assertEqual(h_index([15, 3, 5, 6, 7, 12, 18, 1, 3, 2]), 5)
