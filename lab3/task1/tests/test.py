import time
import unittest
from lab3.utils import read_data, write_data, generations
import tracemalloc
from lab3.task1.src.task1 import randomized_quick_sort

generations("random", 10**3, 0,"C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab3/task1/txtf/input.txt")

def print_time_memory(func):
    n, data = read_data("C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab3/task1/txtf/input.txt")

    tracemalloc.start()
    start_time = time.time()

    func(data, 0, len(data) - 1)

    print("memory usage task 1: ", tracemalloc.get_traced_memory()[1] / 2**20, "Mb")
    print("--- %s seconds ---" % (time.time() - start_time))
    print("\n")
    memory = tracemalloc.get_traced_memory()[1] / 2**20
    times = time.time() - start_time

    tracemalloc.stop()

    write_data(data, "C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab3/task1/txtf/output.txt")
    result = read_data("C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab3/task1/txtf/output.txt")

    return memory, times, result


class TestTask(unittest.TestCase):

    def test_should_check_time_memori_max_value(self):
        n, data = read_data("C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab3/task1/txtf/input.txt")
        expected_result = sorted(data)
        expected_memory = 256
        expected_time = 2
        m, t, result = print_time_memory(randomized_quick_sort)

        self.assertEqual(result, expected_result)
        self.assertLessEqual(t, expected_time, f"Значение {t} превышает порог {expected_time}")
        self.assertLessEqual(m, expected_memory, f"Значение {m} превышает порог {expected_memory}")
