import time
import unittest
from lab3.utils import *
import tracemalloc
from lab3.task2.src.task2 import generate_worst_case

#generation_random_n("C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab3/task2/txtf/input.txt")

def print_time_memory(func):
    n = read_data("C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab3/task2/txtf/input.txt", 2)

    tracemalloc.start()
    start_time = time.time()

    func(n)

    print("memory usage task 2: ", tracemalloc.get_traced_memory()[1] / 2**20, "Mb")
    print("--- %s seconds ---" % (time.time() - start_time))
    print("\n")
    memory = tracemalloc.get_traced_memory()[1] / 2**20
    times = time.time() - start_time

    tracemalloc.stop()

    write_data(func(n), "C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab3/task2/txtf/output.txt")

    return memory, times


class TestTask(unittest.TestCase):

    def test_should_check_time_memori_value(self):
        expected_memory = 256
        expected_time = 2
        m, t  = print_time_memory(generate_worst_case)

        self.assertLessEqual(t, expected_time, f"Значение {t} превышает порог {expected_time}")
        self.assertLessEqual(m, expected_memory, f"Значение {m} превышает порог {expected_memory}")