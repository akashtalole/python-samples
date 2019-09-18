
def coroutine_decorator(func):
    def wrap(*args, **kwargs):
        cr = func(*args, **kwargs)
        cr.next()
        return cr
    return wrap


@coroutine_decorator
def coroutine_example():
    while True:
        x = yield
        #do something with x
        print x
