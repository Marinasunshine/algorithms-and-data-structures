import time
import tracemalloc
import random
from lab2.task2.src.task2 import *

def generate_random_array(low=-10**9, high=10**9):
    n = 10
    random_array = random.sample(range(low, high), n)
    with open('../txtf/input.txt', 'w') as f:
        f.write(f"{n}\n")
        f.write(" ".join(map(str, random_array)))

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