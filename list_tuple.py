# List vs Tuple
# https://www.afternerd.com/blog/difference-between-list-tuple/
# The main difference between lists and a tuples is the fact that lists are
# mutable whereas tuples are immutable.

# Appending performance: Mutability Wins!
# Easiness of debugging: Immutability Wins!
# Memory efficiency: Immutability Wins !

# list -> mutable
print "---list---"
a = ["akash", "test"]
print "a: {}".format(a)

# tuple -> immutable
print "---tuple---"
b = ("akash", "test")
print "b: {}".format(b)

# modify
print "updating list"
a[0] = 'sky'
print "a: {}".format(a)

print "updating tuple"
try:
    b[0] = 'sky'
except Exception as e:
    print "exception: {}".format(e)
    
# ERROR TypeError: 'tuple' object does not support item assignment
print "b: {}".format(b)
