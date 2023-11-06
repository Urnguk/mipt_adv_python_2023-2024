import multiprocessing as mp
import random
import time


def work(data, res):
    while not data.empty():
        x = data.get()
        time.sleep(0.5)
        res.put((x, x**0.5))


if __name__ == "__main__":
    cpu_num = mp.cpu_count() - 1

    start = mp.Queue()
    for i in range(100):
        start.put(random.randint(0, 1000))
    finish = mp.Queue()

    processes = [mp.Process(target=work, args=(start, finish)) for i in range(cpu_num)]
    for proc in processes:
        proc.start()

    for proc in processes:
        proc.join()

    while not finish.empty():
        print(finish.get())

    print("done")