import time
import unittest
from lab5.utils import read_data, write_data_3_6, generations
import tracemalloc
from lab5.task6.src.task6 import priority_queue

#generations("queue", 10, 0,"C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab5/task6/txtf/input.txt")

def print_time_memory(func):
    n, data = read_data("C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab5/task6/txtf/input.txt", 6)

    tracemalloc.start()
    start_time = time.time()

    func(data)

    print("memory usage task 6: ", tracemalloc.get_traced_memory()[1] / 2**20, "Mb")
    print("--- %s seconds ---" % (time.time() - start_time))
    memory = tracemalloc.get_traced_memory()[1] / 2**20
    times = time.time() - start_time

    tracemalloc.stop()

    write_data_3_6(func(data), "C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab5/task6/txtf/output.txt")
    print(n, data)
    print(func(data))
    print("\n")
    return memory, times


class TestTask(unittest.TestCase):

    def test_should_check_time_memori(self):
        expected_memory = 256
        expected_time = 2
        m, t = print_time_memory(priority_queue)

        self.assertLessEqual(t, expected_time, f"Значение {t} превышает порог {expected_time}")
        self.assertLessEqual(m, expected_memory, f"Значение {m} превышает порог {expected_memory}")



