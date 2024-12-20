import time
import unittest
from lab4.utils import read_data, write_data, generations
import tracemalloc
from lab4.task5.src.task5 import stack_max

#generations("stack_max", 5, 0,"C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab4/task5/txtf/input.txt")

def print_time_memory(func):
    n, data = read_data("C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab4/task5/txtf/input.txt", 5)

    tracemalloc.start()
    start_time = time.time()

    func(data)

    print("memory usage task 5: ", tracemalloc.get_traced_memory()[1] / 2**20, "Mb")
    print("--- %s seconds ---" % (time.time() - start_time))
    memory = tracemalloc.get_traced_memory()[1] / 2**20
    times = time.time() - start_time

    tracemalloc.stop()

    write_data(func(data), "C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab4/task5/txtf/output.txt")
    print(n, data)
    print(func(data))
    print("\n")
    return memory, times


class TestTask(unittest.TestCase):

    def test_should_check_time_memori(self):
        expected_memory = 512
        expected_time = 5
        m, t = print_time_memory(stack_max)

        self.assertLessEqual(t, expected_time, f"Значение {t} превышает порог {expected_time}")
        self.assertLessEqual(m, expected_memory, f"Значение {m} превышает порог {expected_memory}")

