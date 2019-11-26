import asyncio

loop = asyncio.get_event_loop()

def callback():
    print("asyncio learning")
    loop.stop()

loop.call_later(1.0, callback)
loop.run_forever()

async def network_request(number):
    await asyncio.sleep(1.0)
    return {"success":True, "result": number ** 2}

async def fetch_square(number):
    response = await network_request(number)
    if response["success"]:
        print("Result is: {}".format(response["result"]))

loop.run_until_complete(fetch_square(3))
loop.run_until_complete(fetch_square(6))
loop.run_until_complete(fetch_square(9))