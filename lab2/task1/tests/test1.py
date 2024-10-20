import time
import tracemalloc
import unittest
from lab2.task1.src.task1 import *

start = time.perf_counter()
tracemalloc.start()

class InsertionSortTestCase(unittest.TestCase):
    def output_design(self, test_num, func, eq_value, params):
        start = time.perf_counter()
        tracemalloc.start()
        self.assertEqual(func(params), eq_value)

        print(f"Тест {test_num}:")
        print("Время работы: %s секунд " % (time.perf_counter() - start))
        print("Затрачено памяти:", tracemalloc.get_traced_memory()[1] / 1024 / 1024, "MB")
        tracemalloc.stop()