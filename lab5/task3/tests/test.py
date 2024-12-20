import time
import unittest
from lab5.utils import read_data, write_data_3_6, generations
import tracemalloc
from lab5.task3.src.task3 import process_packets

generations("packets", 10, 10,"C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab5/task3/txtf/input.txt")

def print_time_memory(func):
    S, n, data = read_data("C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab5/task3/txtf/input.txt", 3)

    tracemalloc.start()
    start_time = time.time()

    func(S, data)

    print("memory usage task 3: ", tracemalloc.get_traced_memory()[1] / 2**20, "Mb")
    print("--- %s seconds ---" % (time.time() - start_time))
    memory = tracemalloc.get_traced_memory()[1] / 2**20
    times = time.time() - start_time

    tracemalloc.stop()

    write_data_3_6(func(S, data), "C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab5/task3/txtf/output.txt")
    print(S, n, data)
    print(func(S, data))
    print("\n")
    return memory, times


class TestTask(unittest.TestCase):

    def test_should_check_time_memori_max_value(self):
        expected_memory = 512
        expected_time = 10
        m, t = print_time_memory(process_packets)

        self.assertLessEqual(t, expected_time, f"Значение {t} превышает порог {expected_time}")
        self.assertLessEqual(m, expected_memory, f"Значение {m} превышает порог {expected_memory}")

    def test_correct_work(self):
        self.assertEqual(process_packets(1, []), [])
        self.assertEqual(process_packets(1, [(0, 0)]), [0])
        self.assertEqual(process_packets(1, [(0, 1), (0, 1)]), [0, -1])
        self.assertEqual(process_packets(1, [(0, 1), (1, 1)]), [0, 1])
        self.assertEqual(process_packets(1, [(0, 0), (0, 0)]), [0, 0])
        self.assertEqual(process_packets(2, [(0, 1), (3, 1), (10, 1)]), [0, 3, 10])
        self.assertEqual(process_packets(3, [(0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2)]), [0, 2, 4, 6, 8, -1])
