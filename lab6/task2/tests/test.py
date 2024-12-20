import time
import unittest
from lab6.utils import read_data, write_data_2, generations
import tracemalloc
from lab6.task2.src.task2 import phonebook_manager

generations("phone", 10, "C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab6/task2/txtf/input.txt")

def print_time_memory(func):
    n, data = read_data("C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab6/task2/txtf/input.txt", 1)

    tracemalloc.start()
    start_time = time.time()

    func(data)

    print("memory usage task 2: ", tracemalloc.get_traced_memory()[1] / 2**20, "Mb")
    print("--- %s seconds ---" % (time.time() - start_time))
    memory = tracemalloc.get_traced_memory()[1] / 2**20
    times = time.time() - start_time

    tracemalloc.stop()

    write_data_2(func(data), "C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab6/task2/txtf/output.txt")
    print(n, data)
    print(func(data))
    print("\n")
    return memory, times


class TestTask(unittest.TestCase):

    def test_should_check_time_memori(self):
        expected_memory = 512
        expected_time = 6
        m, t = print_time_memory(phonebook_manager)

        self.assertLessEqual(t, expected_time, f"Значение {t} превышает порог {expected_time}")
        self.assertLessEqual(m, expected_memory, f"Значение {m} превышает порог {expected_memory}")