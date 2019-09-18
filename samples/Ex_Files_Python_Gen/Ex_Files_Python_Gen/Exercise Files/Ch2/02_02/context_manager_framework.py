# basic contextmanager framework

@contextmanager
def simple_context_manager(obj):
    try:
        #do something
        yield
    finally:
        #wrap up
