import time
import unittest
from lab3.utils import *
import tracemalloc
from lab3.task9.src.task9 import find_closest_pair

#generations("points", 1, 0, "C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab3/task9/txtf/input.txt")

def print_time_memory(func):
    n, points = read_data("C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab3/task9/txtf/input.txt",9)

    tracemalloc.start()
    start_time = time.time()

    func(points)

    print("memory usage task 9: ", tracemalloc.get_traced_memory()[1] / 2**20, "Mb")
    print("--- %s seconds ---" % (time.time() - start_time))
    print("\n")
    memory = tracemalloc.get_traced_memory()[1] / 2**20
    times = time.time() - start_time

    tracemalloc.stop()

    write_data(func(points), "C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab3/task9/txtf/output.txt")

    return memory, times


class TestTask(unittest.TestCase):

    def test_should_check_time_memori_value(self):
        expected_memory = 256
        expected_time = 10
        m, t = print_time_memory(find_closest_pair)

        self.assertLessEqual(t, expected_time, f"Значение {t} превышает порог {expected_time}")
        self.assertLessEqual(m, expected_memory, f"Значение {m} превышает порог {expected_memory}")

    def test_correct_work(self):
        self.assertAlmostEqual(find_closest_pair([(0, 0), (3, 4)]), 5.0000,  places=4)
        self.assertAlmostEqual(find_closest_pair([(7, 7), (1, 100), (4, 8), (7, 7)]), 0.0000,  places=4)
        self.assertAlmostEqual(find_closest_pair([(4, 4), (-2, -2), (-3, -4), (-1, 3), (2, 3), (-4, 0), (1, 1), (-1, -1), (3, -1), (-4, 2), (-2, 4)]), 1.4142,  places=4)
        self.assertAlmostEqual(find_closest_pair([(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0)]), 1.0000,  places=4)
        self.assertAlmostEqual(find_closest_pair([(0, 0), (100, 100), (200, 200), (-100, -100), (50, 50), (60, 60), (70, 70), (80, 80), (90, 90), (55, 55)]), 7.0711,  places=4)
