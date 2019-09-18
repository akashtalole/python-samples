
def coroutine_example():
    while True:
        x = yield
        #do something with x
        print x
