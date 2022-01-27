import time


class StopWatch:

    def calculateTime(self):
        print("process has started")
        start_time = time.time()
        input("press Enter key to start the time ")
        end_time = time.time()
        input("press Enter key to stop the time ")
        elapsed_time = end_time - start_time

obj = StopWatch()
elapseTime = obj.calculateTime()
