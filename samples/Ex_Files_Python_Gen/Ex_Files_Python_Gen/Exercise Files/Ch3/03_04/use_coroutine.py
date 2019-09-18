from coroutine_decorator import coroutine_decorator

def sender(filename, target):
    for line in open(filename):
        target.send(line)
    target.close()
        

@coroutine_decorator
def match_counter(string):
    count = 0
    try:
        while True:
            line = yield
            if string in line:
                count += 1
    except GeneratorExit:
        print '{}: {}'.format(string, count)



@coroutine_decorator
def longer_than(n):
    count = 0
    try:
        while True:
            line = yield
            if len(line)>n:
                print line
                count += 1
    except GeneratorExit:
        print 'longer than {}: {}'.format(n, count)
