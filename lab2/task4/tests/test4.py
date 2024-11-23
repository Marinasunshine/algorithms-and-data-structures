import time
import unittest
from lab2.utils import *
import tracemalloc
from lab2.task4.src.task4 import binary_search

generations("bin", 5, 5,"C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab2/task4/txtf/input.txt")

def print_time_memory(func):
    n, data, k, data2 = read_data("C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab2/task4/txtf/input.txt")

    tracemalloc.start()
    start_time = time.time()

    res = [binary_search(data, x) for x in data2]

    print("memory usage task 4: ", tracemalloc.get_traced_memory()[1] / 2**20, "Mb")
    print("--- %s seconds ---" % (time.time() - start_time))
    print("\n")
    memory = tracemalloc.get_traced_memory()[1] / 2**20
    times = time.time() - start_time

    tracemalloc.stop()

    write_data(res, "C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab2/task4/txtf/output.txt")
    result = read_data("C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab2/task4/txtf/output.txt")

    return memory, times, result


class TestTask(unittest.TestCase):

    def test_should_check_time_memori_value(self):
        n, data, k, data2 = read_data("C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab2/task4/txtf/input.txt")
        expected_result = [binary_search(data, x) for x in data2]
        expected_memory = 256
        expected_time = 2
        m, t, result = print_time_memory(binary_search)

        self.assertEqual(result, expected_result)
        self.assertLessEqual(t, expected_time, f"Значение {t} превышает порог {expected_time}")
        self.assertLessEqual(m, expected_memory, f"Значение {m} превышает порог {expected_memory}")

