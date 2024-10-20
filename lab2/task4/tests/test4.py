import time
import tracemalloc
import random
from lab2.task4.src.task4 import *

def generate_random_array(low=1, high=10**9):
    n = 10
    k = 10
    random_array_n = random.choices(range(low, high), k = n)
    random_array_k = random.choices(range(low, high), k = k)
    with open('../txtf/input.txt', 'w') as f:
        f.write(f"{n}\n")
        f.write(" ".join(map(str, random_array_n)) + "\n")
        f.write(f"{k}\n")
        f.write(" ".join(map(str, random_array_k)) + "\n")

def time_and_memory(func, inp, outp):
    start = time.perf_counter()
    tracemalloc.start()
    func(inp, outp)
    memory = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()
    end = time.perf_counter()

    print(f"Время выполнения: {end - start} секунд")
    print(f"Использование памяти: {memory / 1024 / 1024} MB")

generate_random_array()
time_and_memory(check_and_write, '../txtf/input.txt', '../txtf/output.txt')