import time
import unittest
from lab4.utils import read_data, write_data_7, generations
import tracemalloc
from lab4.task7.src.task7 import find_max

generations("moving_max", 5, 2,"C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab4/task7/txtf/input.txt")

def print_time_memory(func):
    n, data, m = read_data("C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab4/task7/txtf/input.txt", 7)

    tracemalloc.start()
    start_time = time.time()

    func(n, data, m)

    print("memory usage task 7: ", tracemalloc.get_traced_memory()[1] / 2**20, "Mb")
    print("--- %s seconds ---" % (time.time() - start_time))
    memory = tracemalloc.get_traced_memory()[1] / 2**20
    times = time.time() - start_time

    tracemalloc.stop()

    write_data_7(func(n, data, m), "C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab4/task7/txtf/output.txt")
    print(n, data, m)
    print(func(n, data, m))
    print("\n")
    return memory, times


class TestTask(unittest.TestCase):

    def test_should_check_time_memori(self):
        expected_memory = 512
        expected_time = 5
        m, t = print_time_memory(find_max)

        self.assertLessEqual(t, expected_time, f"Значение {t} превышает порог {expected_time}")
        self.assertLessEqual(m, expected_memory, f"Значение {m} превышает порог {expected_memory}")

