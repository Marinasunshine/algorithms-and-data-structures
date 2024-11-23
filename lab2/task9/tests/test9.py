import time
import unittest
from lab2.utils import *
import tracemalloc
from lab2.task9.src.task9 import matrix_mult

generations("matrix", 3,0,"C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab2/task9/txtf/input.txt")

def print_time_memory(func):
    n, A, B = read_data("C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab2/task9/txtf/input.txt")

    tracemalloc.start()
    start_time = time.time()

    print("memory usage task 9: ", tracemalloc.get_traced_memory()[1] / 2**20, "Mb")
    print("--- %s seconds ---" % (time.time() - start_time))
    print("\n")
    memory = tracemalloc.get_traced_memory()[1] / 2**20
    times = time.time() - start_time

    tracemalloc.stop()

    write_data(func(n, A, B), "C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab2/task9/txtf/output.txt")

    return memory, times


class TestTask(unittest.TestCase):

    def test_should_check_time_memori_value(self):
        expected_memory = 256
        expected_time = 2
        m, t = print_time_memory(matrix_mult)

        self.assertLessEqual(t, expected_time, f"Значение {t} превышает порог {expected_time}")
        self.assertLessEqual(m, expected_memory, f"Значение {m} превышает порог {expected_memory}")