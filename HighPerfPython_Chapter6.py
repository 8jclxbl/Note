import time
from datetime import datetime
import threading
from functools import wraps

def wait_and_print(msg):
    time.sleep(1.0)
    print(msg)

#其中的语句不会阻塞程序的执行
def wait_and_print_async(msg):
    def callback():
        print(msg)
    timer = threading.Timer(1.0, callback)
    timer.start()

def  network_request(number):
    time.sleep(1.0)
    return {"success":True, "result": number ** 2}

def on_done(result):
    print(result)

def network_request_async(number, on_done):
    def timer_done():
        on_done({"success":True, "result": number ** 2})
    timer = threading.Timer(1.0, timer_done)
    timer.start()

def fetch_square(number):
    response = network_request(number)
    if response["success"]:
        print("Result is: {}".format(response["result"]))

def fetch_square_async(number):
    def on_done(response):
        if response["success"]:
            print("Result is: {}".format(response["result"]))
    network_request_async(number, on_done)

def timeCount(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        start = datetime.now()
        res = func(*args, **kwargs)
        end = datetime.now()
        print("Func:{}, params:{}; Running time: {}".format(func.__name__,args,end - start))
        return res
    return wrap

@timeCount
def network_request_case(case):
    fetch_square(case)

@timeCount
def network_request_suite():
    network_request_case(2)
    network_request_case(3)
    network_request_case(4)
    print("Submission over")

@timeCount
def network_request_async_case(case):
    fetch_square_async(case)

@timeCount
def network_request_async_suite():
    network_request_async_case(2)
    network_request_async_case(3)
    network_request_async_case(4)
    print("Submission over")

@timeCount
def wait_and_print_case():
    wait_and_print("first")
    wait_and_print("second")

@timeCount
def wait_and_print_async_case():
    wait_and_print_async("first")
    wait_and_print_async("second")

def wait_and_print_compare_test_suite():
    wait_and_print_case()
    wait_and_print_async_case()

if __name__ == "__main__":
    network_request_suite()
    #wait_and_print_compare_test_suite()
    network_request_async_suite()