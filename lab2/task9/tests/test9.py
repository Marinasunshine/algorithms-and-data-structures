import time
import tracemalloc
import random
from lab2.task9.src.task9 import *

def generate_random_array(low=-0, high=100):
    n = 3
    matrixA = [[random.randint(low, high) for _ in range(n)] for _ in range(n)]
    matrixB = [[random.randint(low, high) for _ in range(n)] for _ in range(n)]
    with open('../txtf/input.txt', 'w') as f:
        f.write(f"{n}\n")
        for r in matrixA:
            f.write(" ".join(map(str, r)) + "\n")
        for r in matrixB:
            f.write(" ".join(map(str, r)) + "\n")

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