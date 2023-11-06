import multiprocessing as mp
import time


def work(x):
    time.sleep(1)
    print(x)


if __name__ == "__main__":
    cpu_num = mp.cpu_count() - 1
    # x = mp.Process(target=work, args=(0,))
    processes = [mp.Process(target=work, args=(i,)) for i in range(cpu_num)]
    for proc in processes:
        proc.start()
        # proc.join()
    for proc in processes:
        proc.join()
        # time.sleep(0.1)

    print("done")