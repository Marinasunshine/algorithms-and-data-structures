import time
import unittest
from lab7.utils import read_data, write_data, generations
import tracemalloc
from lab7.task1.src.task1 import min_coins

generations("coins", 10, 5,"C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab7/task1/txtf/input.txt")

def print_time_memory(func):
    money, k, coins = read_data("C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab7/task1/txtf/input.txt", 1)

    tracemalloc.start()
    start_time = time.time()

    func(money, coins)

    print("memory usage task 1: ", tracemalloc.get_traced_memory()[1] / 2**20, "Mb")
    print("--- %s seconds ---" % (time.time() - start_time))
    times = time.time() - start_time

    tracemalloc.stop()

    write_data(func(money, coins), "C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab7/task1/txtf/output.txt")
    print(money, k, coins)
    print(func(money, coins))
    print("\n")
    return times


class TestTask(unittest.TestCase):

    def test_should_check_time(self):
        expected_time = 1
        t= print_time_memory(min_coins)

        self.assertLessEqual(t, expected_time, f"Значение {t} превышает порог {expected_time}")

    def test_coins(self):
        self.assertEqual(min_coins(2, [1, 3, 4]), 2)
        self.assertEqual(min_coins(34, [1, 3, 4]), 9)
        self.assertEqual(min_coins(1000, [1, 3, 4]), 250)
        self.assertEqual(min_coins(0, [1, 3, 4]), 0)
        self.assertEqual(min_coins(7, [2, 5]), 2)
        self.assertEqual(min_coins(10, [1, 2, 2, 5]), 2)

