from concurrent.futures import Future
from datetime import datetime
from threading import Timer
from HighPerfPython_Chapter6 import timeCount

def network_request_async(number):
    future = Future()
    result = {"success":True, "result": number ** 2}
    timer = Timer(1.0, lambda: future.set_result(result))
    timer.start()
    return future

def fetch_square(number):
    fur = network_request_async(number)

    def on_done_future(future):
        response = future.result()
        if response.get("success",False):
            print("the result is {}".format(response["result"]))
    fur.add_done_callback(on_done_future)


#一个简单地轮询
#一个Timer 列表
#构造新的Timer 加入列表
#外层死循环
#   内层Timer列表遍历
#       如果Timer状态发生了改变
#           将该Timer移出
#   如果Timer 列表为空，跳出循环



@timeCount
def test():
    start_ = datetime.now()
    fetch_square(2)
    fetch_square(4)
    end_ = datetime.now()

    print("time used = {}".format(end_ - start_))

if __name__ == "__main__":
    test()
