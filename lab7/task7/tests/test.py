import time
import unittest
from lab7.utils import read_data, write_data, generations
import tracemalloc
from lab7.task7.src.task7 import is_match

#generations("pattern", 5, 5,"C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab7/task7/txtf/input.txt")

def print_time_memory(func):
    pattern, s = read_data("C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab7/task7/txtf/input.txt", 7)

    tracemalloc.start()
    start_time = time.time()

    func(pattern, s)

    print("memory usage task 7: ", tracemalloc.get_traced_memory()[1] / 2**20, "Mb")
    print("--- %s seconds ---" % (time.time() - start_time))
    memory = tracemalloc.get_traced_memory()[1] / 2**20
    times = time.time() - start_time

    tracemalloc.stop()

    write_data(func(pattern, s), "C:/Users/zabot/.virtualenvs/algorithms-and-data-structures/lab7/task7/txtf/output.txt")
    print(pattern, s)
    print(func(pattern, s))
    print("\n")
    return memory, times


class TestTask(unittest.TestCase):

    def test_should_check_time_memori(self):
        expected_memory = 256
        expected_time = 2
        m, t = print_time_memory(is_match)

        self.assertLessEqual(t, expected_time, f"Значение {t} превышает порог {expected_time}")
        self.assertLessEqual(m, expected_memory, f"Значение {m} превышает порог {expected_memory}")

    def test_match(self):
        self.assertEqual(is_match("abcd", "xyz"), "NO")
        self.assertEqual(is_match("a?c", "abcde"), "NO")
        self.assertEqual(is_match("a*", "abc"), "YES")
        self.assertEqual(is_match("b*", "abc"), "NO")
        self.assertEqual(is_match("a*b*c", "abc"), "YES")
        self.assertEqual(is_match("a*b*c", "abbbbc"), "YES")
        self.assertEqual(is_match("a?b*", "abc"), "NO")
        self.assertEqual(is_match("a?b*", "acb"), "YES")



