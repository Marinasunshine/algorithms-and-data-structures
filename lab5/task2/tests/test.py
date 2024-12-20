import time
import unittest
from lab5.utils import read_data, write_data, generations
import tracemalloc
from lab5.task2.src.task2 import find_height

generations("tree", 10, 0,"C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab5/task2/txtf/input.txt")

def print_time_memory(func):
    n, data = read_data("C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab5/task2/txtf/input.txt", 1)

    tracemalloc.start()
    start_time = time.time()

    func(data, n)

    print("memory usage task 2: ", tracemalloc.get_traced_memory()[1] / 2**20, "Mb")
    print("--- %s seconds ---" % (time.time() - start_time))
    memory = tracemalloc.get_traced_memory()[1] / 2**20
    times = time.time() - start_time

    tracemalloc.stop()

    write_data(func(data, n), "C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab5/task2/txtf/output.txt")
    print(n, data)
    print(func(data, n))
    print("\n")
    return memory, times


class TestTask(unittest.TestCase):

    def test_should_check_time_memori_max_value(self):
        expected_memory = 512
        expected_time = 3
        m, t = print_time_memory(find_height)

        self.assertLessEqual(t, expected_time, f"Значение {t} превышает порог {expected_time}")
        self.assertLessEqual(m, expected_memory, f"Значение {m} превышает порог {expected_memory}")

    def test_correct_work(self):
        self.assertEqual(find_height([4, -1, 4, 1, 1], 5), 3)
        self.assertEqual(find_height([-1, 0, 4, 0, 3], 5), 4)
        self.assertEqual(find_height([1, -1, 2], 3), 2)
        self.assertEqual(find_height([-1], 1), 1)
        self.assertEqual(find_height([-1, 2, 5, 4, 5, 0], 6), 4)
        self.assertEqual(find_height([3, -1, 1, 1, 1, 1], 6), 3)




