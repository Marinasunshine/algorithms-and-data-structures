import time
import unittest
from lab2.utils import *
import tracemalloc
from lab2.task1.src.task1 import merge_sort

generations("random", 5, 0,"C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab2/task1/txtf/input.txt")

def print_time_memory(func):
    n, data = read_data("C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab2/task1/txtf/input.txt")

    tracemalloc.start()
    start_time = time.time()

    func(data)

    print("memory usage task 1: ", tracemalloc.get_traced_memory()[1] / 2**20, "Mb")
    print("--- %s seconds ---" % (time.time() - start_time))
    memory = tracemalloc.get_traced_memory()[1] / 2**20
    times = time.time() - start_time

    tracemalloc.stop()

    write_data(func(data), "C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab2/task1/txtf/output.txt")
    result = read_data("C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab2/task1/txtf/output.txt")
    print(n, data)
    print(func(data))
    print("\n")
    return memory, times, result


class TestTask(unittest.TestCase):

    def test_should_check_time_memori_value(self):
        n, data = read_data("C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab2/task1/txtf/input.txt")
        expected_result = sorted(data)
        expected_memory = 256
        expected_time = 2
        m, t, result = print_time_memory(merge_sort)

        self.assertEqual(result, expected_result)
        self.assertLessEqual(t, expected_time, f"Значение {t} превышает порог {expected_time}")
        self.assertLessEqual(m, expected_memory, f"Значение {m} превышает порог {expected_memory}")

    def test_correct_work(self):
        self.assertEqual(merge_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([5, 5, 5, 5]), [5, 5, 5, 5])
        self.assertEqual(merge_sort([1, 3, 0]), [0, 1, 3])
        self.assertEqual(merge_sort([0, 0, 0]), [0, 0, 0])
        self.assertEqual(merge_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

if __name__ == "__main__":
    unittest.main()