import time
import unittest
from lab7.utils import read_data, write_data, generations
import tracemalloc
from lab7.task6.src.task6 import longest_lengths

#generations("max", 5, 0,"C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab7/task6/txtf/input.txt")

def print_time_memory(func):
    n, data = read_data("C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab7/task6/txtf/input.txt", 6)

    tracemalloc.start()
    start_time = time.time()

    func(data)

    print("memory usage task 6: ", tracemalloc.get_traced_memory()[1] / 2**20, "Mb")
    print("--- %s seconds ---" % (time.time() - start_time))
    memory = tracemalloc.get_traced_memory()[1] / 2**20
    times = time.time() - start_time

    tracemalloc.stop()

    write_data(func(data), "C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab7/task6/txtf/output.txt")
    print(n, data)
    print(func(data))
    print("\n")
    return memory, times


class TestTask(unittest.TestCase):

    def test_should_check_time_memori(self):
        expected_memory = 256
        expected_time = 2
        m, t = print_time_memory(longest_lengths)

        self.assertLessEqual(t, expected_time, f"Значение {t} превышает порог {expected_time}")
        self.assertLessEqual(m, expected_memory, f"Значение {m} превышает порог {expected_memory}")

    def test_longest_lengths(self):
        self.assertEqual(longest_lengths([3, 29, 5, 5, 28, 6]), (3, [3, 5, 28]))
        self.assertEqual(longest_lengths([10]), (1, [10]))
        self.assertEqual(longest_lengths([1, 2, 3, 4, 5]), (5, [1, 2, 3, 4, 5]))
        self.assertEqual(longest_lengths([5, 4, 3, 2, 1]), (1, [5]))
        self.assertEqual(longest_lengths([10, 9, 2, 5, 3, 7, 101, 18]), (4, [2, 5, 7, 101]))

