import time
import unittest
from lab7.utils import read_data, write_data, generations
import tracemalloc
from lab7.task4.src.task4 import length

#generations("sequence", 5, 5,"C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab7/task4/txtf/input.txt")

def print_time_memory(func):
    a, data, b, data2 = read_data("C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab7/task4/txtf/input.txt", 4)

    tracemalloc.start()
    start_time = time.time()

    func(data, data2)

    print("memory usage task 4: ", tracemalloc.get_traced_memory()[1] / 2**20, "Mb")
    print("--- %s seconds ---" % (time.time() - start_time))
    times = time.time() - start_time

    tracemalloc.stop()

    write_data(func(data, data2), "C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab7/task4/txtf/output.txt")
    print(a, data, b, data2)
    print(func(data, data2))
    print("\n")
    return times


class TestTask(unittest.TestCase):

    def test_should_check_time_memori_max_value(self):
        expected_time = 1
        t = print_time_memory(length)

        self.assertLessEqual(t, expected_time, f"Значение {t} превышает порог {expected_time}")

    def test_length(self):
        self.assertEqual(length([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]), 5)
        self.assertEqual(length([2, 7, 5], [2, 5]), 2)
        self.assertEqual(length([1, 2, 3, 4], [5, 2, 8, 7]), 1)
        self.assertEqual(length([2, 7, 8, 3], [5, 2, 8, 7]), 2)
        self.assertEqual(length([10], [10]), 1)
        self.assertEqual(length([1, 2, 3], [4, 5, 6]), 0)


