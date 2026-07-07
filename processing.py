# import multiprocessing
# import time


# def worker(interval, name):
#     print(name + '【start】')
#     # time.sleep(interval)
#     print(name + '【end】')


# if __name__ == "__main__":
#     p1 = multiprocessing.Process(target=worker, args=(2, '两点水1'))
#     p2 = multiprocessing.Process(target=worker, args=(3, '两点水2'))
#     p3 = multiprocessing.Process(target=worker, args=(4, '两点水3'))

#     p1.start()
#     p2.start()
#     p3.start()

#     print("The number of CPU is:" + str(multiprocessing.cpu_count()))
#     for p in multiprocessing.active_children():
#         print("child   p.name:" + p.name + "\tp.id" + str(p.pid))
#     print("END!!!!!!!!!!!!!!!!!")

# import multiprocessing
# import time


# class ClockProcess(multiprocessing.Process):
#     def __init__(self, interval):
#         multiprocessing.Process.__init__(self)
#         self.interval = interval

#     def run(self):
#         n = 5
#         while n > 0:
#             print(f"当前时间: {time.ctime()}")
#             time.sleep(self.interval)
#             n -= 1


# if __name__ == '__main__':
#     p = ClockProcess(3)
#     p.start()

from multiprocessing import Pool
import os
import time
import random


def long_time_task(name):
    print(f'进程的名称：{name} ；进程的 PID: {os.getpid()} ')
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print(f'进程 {name} 运行了 {end - start} 秒')


if __name__ == '__main__':
    print(f'主进程的 PID：{os.getpid()}')
    p = Pool(6)
    for i in range(6):
        p.apply(long_time_task, args=(i,))
    p.close()
    # 等待所有子进程结束后再关闭主进程
    # p.join()
    print('【End】')