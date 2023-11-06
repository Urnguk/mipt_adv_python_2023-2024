import multiprocessing as mp
import time


def work(x):
    time.sleep(0.5)
    return x**0.5


if __name__ == "__main__":
    cpu_num = mp.cpu_count() - 1
    p = mp.Pool(cpu_num)

    data = [i for i in range(100)]
    res = p.map(work, data)
    print(type(res))
    print(*res)