import time
import unittest
from lab2.utils import *
import tracemalloc
from lab2.task9.src.task9_1 import strassen

generations("matrix", 4, 0,"C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab2/task9/txtf/input.txt")

def print_time_memory(func):
    n, A, B = read_data("C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab2/task9/txtf/input.txt")

    tracemalloc.start()
    start_time = time.time()

    func(A, B)

    print("memory usage task 9_1: ", tracemalloc.get_traced_memory()[1] / 2**20, "Mb")
    print("--- %s seconds ---" % (time.time() - start_time))
    memory = tracemalloc.get_traced_memory()[1] / 2**20
    times = time.time() - start_time

    tracemalloc.stop()

    write_data(func(A, B), "C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab2/task9/txtf/output.txt")
    print(n, A, B)
    print(func(A, B))
    print("\n")
    print("----------------------")
    return memory, times


class TestTask(unittest.TestCase):

    def test_should_check_time_memori_value(self):
        expected_memory = 256
        expected_time = 2
        m, t = print_time_memory(strassen)

        self.assertLessEqual(t, expected_time, f"Значение {t} превышает порог {expected_time}")
        self.assertLessEqual(m, expected_memory, f"Значение {m} превышает порог {expected_memory}")

if __name__ == "__main__":
    unittest.main()