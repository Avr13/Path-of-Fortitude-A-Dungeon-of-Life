import threading
import time
import sys
import os


if sys.version_info[0] < 3:
    input = raw_input

def game():
    class SecondCounter(threading.Thread):

        def __init__(self, interval=0.001):
            # init the thread
            threading.Thread.__init__(self)
            self.interval = interval  # seconds
            # initial value
            self.value = 0
            # controls the while loop in method run
            self.alive = False

        def run(self):
            self.alive = True
            while self.alive:
                time.sleep(self.interval)
                # update count value
                self.value += self.interval

        def peek(self):
            return self.value

        def finish(self):
            self.alive = False
            return self.value

    ts = 0
    count = SecondCounter()

    count.start()


    for i in range(30):
        e = input("Press Enter Rapidly")
        os.system('cls')

    seconds = count.finish()
    ts = ts + seconds

    return ts
    # return("You took {} seconds".format(ts))