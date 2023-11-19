import threading
import time

def test():
    time.sleep(5)
    print("hallo")

def test_start_thread():
    t1 = threading.Thread(target=test,args=())
    t1.start()

def run():
    test_start_thread()

    print("hallo2")

run()