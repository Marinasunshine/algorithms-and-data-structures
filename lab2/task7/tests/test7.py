import time
import unittest
from lab2.utils import *
import tracemalloc
from lab2.task7.src.task7 import max_sub

generations("random", 5, 0,"C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab2/task7/txtf/input.txt")

def print_time_memory(func):
    n, data = read_data("C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab2/task7/txtf/input.txt")

    tracemalloc.start()
    start_time = time.time()

    func(data)

    print("memory usage task 7: ", tracemalloc.get_traced_memory()[1] / 2**20, "Mb")
    print("--- %s seconds ---" % (time.time() - start_time))
    memory = tracemalloc.get_traced_memory()[1] / 2**20
    times = time.time() - start_time

    tracemalloc.stop()

    write_data(func(data), "C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab2/task7/txtf/output.txt")
    print(n, data)
    print(func(data))
    print("\n")
    return memory, times


class TestTask(unittest.TestCase):

    def test_should_check_time_memori_value(self):
        expected_memory = 256
        expected_time = 2
        m, t = print_time_memory(max_sub)

        self.assertLessEqual(t, expected_time, f"Значение {t} превышает порог {expected_time}")
        self.assertLessEqual(m, expected_memory, f"Значение {m} превышает порог {expected_memory}")

    def test_correct_work(self):
        self.assertEqual(max_sub([-2, 1, -3, 4, -1, 2, 1, -5, 4]), [4, -1, 2, 1])
        self.assertEqual(max_sub([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(max_sub([10]), [10])
        self.assertEqual(max_sub([5, -3, 4, -1, 2, -4, 6, -1, -2, 3]), [5, -3, 4, -1, 2, -4, 6])

if __name__ == "__main__":
    unittest.main()
