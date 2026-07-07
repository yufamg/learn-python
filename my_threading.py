import time
import threading


class MyThread(threading.Thread):
    def run(self):
        for i in range(5):
            print(f'thread {self.name}, @number: {i}')
            time.sleep(1)


def main():
    print("Start main threading")

    threads = [MyThread() for i in range(3)]
    for t in threads:
        t.start()

    # 依次让新创建的线程执行 join
    for t in threads:
        t.join()

    print("End Main threading")


if __name__ == '__main__':
    main()