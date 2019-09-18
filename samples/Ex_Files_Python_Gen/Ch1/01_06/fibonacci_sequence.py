# Fibonacci Sequence Generator

def fibonacci_gen():
    trailing, lead = 0,1
    while True:
    	yield lead
    	trailing, lead = lead, trailing+lead

