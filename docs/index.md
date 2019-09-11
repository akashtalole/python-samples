## Python Concepts

# What is Python? Executive Summary
- Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. 
- Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together. 
- Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance. 
- Python supports modules and packages, which encourages program modularity and code reuse. 
- The Python interpreter and the extensive standard library are available in source or binary form without charge for all major platforms, and can be freely distributed.
- Often, programmers fall in love with Python because of the increased productivity it provides. 
- Since there is no compilation step, the edit-test-debug cycle is incredibly fast. 
- Debugging Python programs is easy: a bug or bad input will never cause a segmentation fault. Instead, when the interpreter discovers an error, it raises an exception. When the program doesn't catch the exception, the interpreter prints a stack trace. 
- A source level debugger allows inspection of local and global variables, evaluation of arbitrary expressions, setting breakpoints, stepping through the code a line at a time, and so on. 
- The debugger is written in Python itself, testifying to Python's introspective power. 
- On the other hand, often the quickest way to debug a program is to add a few print statements to the source: the fast edit-test-debug cycle makes this simple approach very effective.

# Interpreter vs Compiler

| Interpreter | Compiler |
| ----------- | -------- |
| Translates program one statement at a time. | Scans the entire program and translates it as a whole into machine code. |
| It takes less amount of time to analyze the source code but the overall execution time is slower. | It takes large amount of time to analyze the source code but the overall execution time is comparatively faster. |
| No intermediate object code is generated, hence are memory efficient. | Generates intermediate object code which further requires linking, hence requires more memory. |
| Continues translating the program until the first error is met, in which case it stops. Hence debugging is easy. | It generates the error message only after scanning the whole program. Hence debugging is comparatively hard. |
| Programming language like Python, Ruby use interpreters. | Programming language like C, C++ use compilers. |

# Data structure 

# List vs Tuples

| List | Tuples |
| ----------- | -------- |
| Lists are mutable i.e they can be edited.	| Tuples are immutable (tuples are lists which can’t be edited). |
| Lists are slower than tuples.	| Tuples are faster than list. |
| Syntax: list_1 = [10, ‘Chelsea’, 20] | Syntax: tup_1 = (10, ‘Chelsea’ , 20) |

Tuples are used to collect an immutable ordered list of elements. This means that:

- You can’t add elements to a tuple. There’s no append() or extend() method for tuples,
- You can’t remove elements from a tuple. Tuples have no remove() or pop() method,
- You can find elements in a tuple since this doesn’t change the tuple.
- You can also use the in operator to check if an element exists in the tuple.

So, if you’re defining a constant set of values and all you’re going to do with it is iterate through it, use a tuple instead of a list. It will be faster than working with lists and also safer, as the tuples contain “write-protect” data.

# Lists Versus Dictionaries

- A list stores an ordered collection of items, so it keeps some order. Dictionaries don’t have any order.
Dictionaries are known to associate each key with a value, while lists just contain values.

- Use a dictionary when you have an unordered set of unique keys that map to values.

Note that, because you have keys and values that link to each other, the performance will be better than lists in cases where you’re checking membership of an element.

# Lists Versus Sets

- Just like dictionaries, sets have no order in their collection of items. Not like lists.
- Set requires the items contained in it to be hashable, lists store non-hashable items.
- Sets require your items to be unique and immutable. Duplicates are not allowed in sets, while lists allow for duplicates and are mutable.

You should make use of sets when you have an unordered set of unique, immutable values that are hashable.

Take a look below just to be sure:

| Hashable | Non-hashable |
| ----------- | -------- |
| Floats | Dictionaries |
| Integers | Sets |
| Tuple | Lists |
| Strings | |
| frozenset() | |

```
# Import the `collections` library
import collections

# Check if a dictionary is hashable
print(isinstance({}, collections.Hashable))
>> False

# Check if a float is hashable
print(isinstance(0.125, collections.Hashable))
>> True
```

# Variable vs Object

Variable is nothing but a reference to the actual python object in memory.

1. What is Python? What are the benefits of using Python?

Python is a programming language with objects, modules, threads, exceptions and automatic memory management. The benefits of pythons are that it is simple and easy, portable, extensible, build-in data structure and it is an open source.

2. What are the key features of Python?

- Python is an **interpreted** language. That means that, unlike languages like C and its variants, Python does not need to be compiled before it is run. Other interpreted languages include PHP and Ruby.
- Python is **dynamically typed**, this means that you don’t need to state the types of variables when you declare them or anything like that. You can do things like x=111 and then x="I'm a string" without error
- Python is well suited to **object orientated programming** in that it allows the definition of classes along with composition and inheritance. Python does not have access specifiers (like C++’s public, private).
- In Python, **functions** are **first-class objects**. This means that they can be assigned to variables, returned from other functions and passed into functions. Classes are also first class objects
- **Writing Python code is quick** but **running** it is often **slower than compiled languages**. Fortunately，Python allows the inclusion of C based extensions so bottlenecks can be optimized away and often are. The numpy package is a good example of this, it’s really quite quick because a lot of the number crunching it does isn’t actually done by Python
- Python finds **use in many spheres** – web applications, automation, scientific modeling, big data applications and many more. It’s also often used as “glue” code to get other languages and components to play nice.

3. What type of language is python? Programming or scripting?

Python is capable of **scripting**, but in general sense, it is considered as a **general-purpose programming language**.

4. How is Python an interpreted language?

An interpreted language is any programming language which is **not in machine level code before runtime**. Therefore, Python is an interpreted language.

5. What is pep 8?

PEP stands for **Python Enhancement Proposal**. It is a set of rules that specify how to format Python code for maximum readability. PEP 8 is a coding convention, a set of recommendation, about how to write your Python code more readable.

6. How is memory managed in Python?

- Memory management in python is managed by **Python private heap space**. All Python objects and data structures are located in a private heap. The programmer does not have access to this private heap. The python interpreter takes care of this instead.
- The allocation of heap space for Python objects is done by **Python’s memory manager**. The core API gives access to some tools for the programmer to code.
- Python also has an **inbuilt garbage collector**, which **recycles all the unused memory** and so that it can be made available to the heap space.

7. What is namespace in Python?

A namespace is a naming system used to make sure that names are unique to avoid naming conflicts.

```
# var1 is in the global namespace  
var1 = 5
def some_func(): 
  
    # var2 is in the local namespace  
    var2 = 6
    def some_inner_func(): 
  
        # var3 is in the nested local  
        # namespace 
        var3 = 7
```

8. What is PYTHONPATH?

It is an **environment variable** which is used when a module is imported. Whenever a module is imported, PYTHONPATH is also looked up to check for the presence of the imported modules in various directories. The interpreter uses it to determine which module to load.

9. What are python modules? Name some commonly used built-in modules in Python?

Python modules are files containing Python code. This code can either be functions classes or variables. A Python module is a .py file containing executable code.

Some of the commonly used built-in modules are:

os
sys
math
random
datetime
JSON

10. What are local variables and global variables in Python?
Global Variables:

Variables declared outside a function or in global space are called global variables. These variables can be accessed by any function in the program.

Local Variables:

Any variable declared inside a function is known as a local variable. This variable is present in the local space and not in the global space.

```
a=2 #global
def add():
	b=3 #local
	c=a+b
	print(c)
add()
```

11. Is python case sensitive?

Yes. Python is a case sensitive language.

```
a = 10
print a  # this will work
print A  # this will not
```

12. What is type conversion in Python?

Type conversion refers to the conversion of one data type into another.
int() – converts any data type into integer type
float() – converts any data type into float type
ord() – converts characters into integer
hex() – converts integers to hexadecimal
oct() – converts integer to octal
tuple() – This function is used to convert to a tuple
set() – This function returns the type after converting to set.
list() – This function is used to convert any data type to a list type.
dict() – This function is used to convert a tuple of order (key,value) into a dictionary.
str() – Used to convert integer into a string.
complex(real,imag) – This functionconverts real numbers to complex(real,imag) number.

13. Why Python?

14. Shallow copy vs deep copy

14. collection

15. serializer deserilizer

16. How to connect to database in Django?

17. Database engine 

18. How to copy object in python?

Python Lists – Negative Indexing, Slicing, Stepping, Comparing, Max and Min

19. What is negative indexing in python?

The negative indexing starts from where the array ends. This means that the last element of the array is the first element in the negative indexing which is -1.

```
names = ['Ajay', 'Bobby','Ashok', 'Vijay', 'Anil', 'Rahul','Alex', 'Christopher']
print(names[-2])
>>Alex
```

20. What is slicing in python?

Slicing lists helps in fetching sections (slices) of the list. This is a very useful command to get a partial list from a parent list.

```
lst [start:end] # Items from index=start to index=end-1
lst [start:]    # Items index=start through the rest of the array
lst [:end]      # All items from the beginning through index=end-1
lst [:]         # A copy of the whole array
```

There is also a step parameter that you can provide. Mentioning the step parameter will pick only those elements that are at that step. This is useful when you want to skip few inner elements that match the stepping pattern.

```
lst [start:end:step] # Items from index=start to index=end-1 with a step
```
```
lst = ['Ajay', 'Bobby','Ashok', 'Vijay', 'Anil', 'Rahul','Alex', 'Christopher']
print(lst[2:4]) # [‘Ashok’, ‘Vijay’]
print (lst[1:]) # ['Bobby', 'Ashok', 'Vijay', 'Anil', 'Rahul', 'Alex', 'Christopher']
print (lst[0:]) # ['Ajay', 'Bobby', 'Ashok', 'Vijay', 'Anil', 'Rahul', 'Alex', 'Christopher']
print (lst[2:-2]) # ['Ashok', 'Vijay', 'Anil', 'Rahul'] all elements starting from third element but skips the last two elements.
print (lst[::2])  # ['Ashok', 'Vijay', 'Anil', 'Rahul'] this will print all alternate elements (begin to end in steps of 2)
print (lst[::-1]) # ['Christopher', 'Alex', 'Rahul', 'Anil', 'Vijay', 'Ashok', 'Bobby', 'Ajay'] this will print all elements in reverse order

```

https://www.datacamp.com/community/tutorials/18-most-common-python-list-questions-learn-python

21. How To Randomly Select An Element In A List

You can select a random element from your list with the random package:
```
# Import `choice` from the `random` library
from random import choice

# Construct your `list` variable with a list of the first 4 letters of the alphabet
list = ['a', 'b', 'c', 'd']

# Print your random 'list' element
print(choice(list))
```

22. How To Get The first and Last Element Of A List In Your List?

```
a = [1,2,3]
print(a[0]) # first element
print(a[-1]) # last element
```

23. How To Transform Python Lists Into Other Data Structures?

- How To Convert A List To A String?
```
# List of Strings to a String
listOfStrings = ['One', 'Two', 'Three']
strOfStrings = ''.join(listOfStrings)
print(strOfStrings)
>>> OneTwoThree

# List Of Integers to a String
listOfNumbers = [1, 2, 3]
strOfNumbers = ''.join(str(n) for n in listOfNumbers)
print(strOfNumbers)
>>> 23
```

- How To Convert A List To A Tuple

You can change a list to a tuple in Python by using the tuple() function. Pass your list to this function, and you will get a tuple back!

```
# List of Strings to a String
listOfStrings = ['One', 'Two', 'Three']

# Pass your list to `tuple()`
print(tuple(listOfStrings))
>> ('One', 'Two', 'Three')
```

- How To Convert Your List To A Set In Python
```
# List of Strings to a String
listOfStrings = ['One', 'Two', 'Three'] 

# Transform your list into a set
print(set(listOfStrings))
>> {'Three', 'Two', 'One'}
```

- How To Convert Lists To A Dictionaries
A dictionary works with keys and values, so the conversion from a list to a dictionary might be less straightforward.
```
helloWorld = ['hello','world','1','2']
print(list(zip(helloWorld)))
>> [('hello',), ('world',), ('1',), ('2',)]

# Convert to a dictionary
helloWorldDictionary = dict(zip(helloWorld[0::2], helloWorld[1::2]))

# Print out the result
print(helloWorldDictionary)
>> {'hello': 'world', '1': '2'}
```

24. How To Determine The Size Of Your List in Python?

You can pass your list to the len() function to get the length of your list back.
```
# Pass `List` to `len()`
List = [1,2,3,4,5]
len(List)
>> 5
```

25. What’s The Difference Between The Python append() and extend() Methods?

```
# Append [4,5] to `shortList`
shortList.append([4, 5])

# Use the `print()` method to show `shortList`
print(shortList)

# Extend `longerList` with [4,5]
longerList.extend([4, 5])

# Use the `print()` method to see `longerList`
print(longerList)
```

26. How To Concatenate Lists in Python?

To concatenate lists, you use the + operator. It will give you a new list that is the concatenation of your two lists without modifying the original ones.

```
# Concatenate `shortList` with `[4,5]`
plusList = shortList + [4,5]

#Use the `print()` method to see `plusList`
print(plusList)
>> [1, 2, 3, 4, 5]
```

27. How To Sort a List in Python?

```
# Use `sort()` on the `rooms` list
rooms.sort()

# Print out `rooms` to see the result
print(rooms)

# Now use the `sorted()` function on the `orders` list
sorted(orders)

# Print out orders
print(orders)
```

28. How To Clone Or Copy A List in Python?

There are a lot of ways of cloning or copying a list:

- You can slice your original list and store it into a new variable: newList = oldList[:]
- You can use the built-in list() function: newList = list(oldList)
- You can use the copy library:
- With the copy() method: newList = copy.copy(oldList)
- If your list contains objects and you want to copy those as well, you can use copy.deepcopy(): copy.deepcopy(oldList)

```
# Copy the grocery list by slicing and store it in the `newGroceries` variable
newGroceries = groceries[:]
# Copy the grocery list with the `list()` function and store it in a `groceriesForFriends` variable
groceriesForFriends = list(groceries)
# Import the copy library
import copy as c
# Create a `groceriesForFamily` variable and assign the copied grocery list to it
groceriesForFamily = c.copy(groceries)
# Use `deepcopy()` and assign the copied list to a `groceriesForKids` variable
groceriesForKids = c.deepcopy(groceries)
```

29. How Does List Comprehension Work In Python?

List comprehension is, basically speaking, a way of elegantly constructing your lists. The best thing about this for those who love math is the fact that they look a lot like mathematical lists.

```
[x**2 for x in range(10)]
>> [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

30. What is pickling and unpickling?

- Pickle module accepts any Python object and converts it into a string representation and dumps it into a file by using dump function, this process is called pickling. While the process of retrieving original Python objects from the stored string representation is called unpickling.
- The pickle module implements a fundamental, but powerful algorithm for serializing and de-serializing a Python object structure.
- Pickling - is the process whereby a Python object hierarchy is converted into a byte stream, and Unpickling - is the inverse operation, whereby a byte stream is converted back into an object hierarchy.
- Pickling (and unpickling) is alternatively known as serialization, marshalling, or flattening.

31. Is indentation required in python?

- Indentation is necessary for Python. It specifies a block of code. All code within loops, classes, functions, etc is specified within an indented block. It is usually done using four space characters. If your code is not indented necessarily, it will not execute accurately and will throw errors as well.

32. What is the difference between Python Arrays and lists?

- Arrays and lists, in Python, have the same way of storing data. But, arrays can hold only a single data type elements whereas lists can hold any data type elements.

```
import array as arr
My_Array=arr.array('i',[1,2,3,4])
My_list=[1,'abc',1.20]
print(My_Array)
>> array(‘i’, [1, 2, 3, 4])
print(My_list)
>> [1, ‘abc’, 1.2]
```

33. What are functions in Python?

- A function is a block of code which is executed only when it is called.

```
def funct():
	print("hi akash")
funct()
```

34. What is __init__?

- "__init__" is a reseved method in python classes. It is called as a constructor in object oriented terminology. This method is called when an object is created from a class and it allows the class to initialize the attributes of the class.

```
class Employee:
	def __init__(self, name, age,salary):
		self.name = name
		self.age = age
		self.salary = 20000

E1 = Employee("XYZ", 23, 20000) # E1 is the instance of class Employee.

#__init__ allocates memory for E1. 
print(E1.name)
>> XYZ
print(E1.age)
>> 23
print(E1.salary)
>> 20000
```

35. What is self? 

- The word 'self' is used to represent the instance of a class. By using the "self" keyword we access the attributes and methods of the class in python.

36. What is a lambda function?

- In Python, anonymous function means that a function is without a name. As we already know that def keyword is used to define the normal functions and the lambda keyword is used to create anonymous functions. It has the following syntax:

```
lambda arguments: expression
```

- This function can have any number of arguments but only one expression, which is evaluated and returned.
- One is free to use lambda functions wherever function objects are required.
- You need to keep in your knowledge that lambda functions are syntactically restricted to a single expression.
- It has various uses in particular fields of programming besides other types of expressions in functions.

```
# Normal Function
def add(x, y):
	return x+y
print(add(5,6))
>> 11

# lambda function
a = lambda x,y : x+y
print(a(5, 6))
>> 11
```

- Lambda functions can be used along with built-in functions like filter(), map() and reduce().

37. What is filter() in python?

- The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.

- Syntax
```
filter(function, sequence)
Parameters:
function: function that tests if each element of a 
sequence true or not.
sequence: sequence which needs to be filtered, it can 
be sets, lists, tuples, or containers of any iterators.
Retruns:
returns an iterator that is already filtered.
```

- Example
```
# function that filters vowels 
def fun(variable): 
	letters = ['a', 'e', 'i', 'o', 'u'] 
	if (variable in letters): 
		return True
	else: 
		return False


# sequence 
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r'] 

# using filter function 
filtered = filter(fun, sequence) 

print('The filtered letters are:') 
for s in filtered: 
	print(s) 
```

- Output
```
The filtered letters are:
e
e
```

- Application

It is normally used with Lambda functions to separate list, tuple, or sets.
```
# a list contains both even and odd numbers. 
seq = [0, 1, 2, 3, 5, 8, 13] 

# result contains odd numbers of the list 
result = filter(lambda x: x % 2, seq) 
print(list(result)) 
>> [1, 3, 5, 13]

# result contains even numbers of the list 
result = filter(lambda x: x % 2 == 0, seq) 
print(list(result)) 
>> [0, 2, 8]
```

38. What is map() in python?

- map() function returns a list of the results after applying the given function to each item of a given iterable (list, tuple etc.)

- Syntax

```
map(fun, iter)
```
- fun : It is a function to which map passes each element of given iterable.
- iter : It is a iterable which is to be mapped.
- Returns a list of the results after applying the given function to each item of a given iterable (list, tuple etc.)

**NOTE** : You can pass one or more iterable to the map() function. The returned value from map() (map object) then can be passed to functions like list() (to create a list), set() (to create a set) .

```
# Python program to demonstrate working 
# of map. 

# Return double of n 
def addition(n): 
	return n + n 

# We double all numbers using map() 
numbers = (1, 2, 3, 4) 
result = map(addition, numbers) 
print(list(result)) 
>> {2, 4, 6, 8}
```

- We can also use lambda expressions with map to achieve above result.
```
# Double all numbers using map and lambda 

numbers = (1, 2, 3, 4) 
result = map(lambda x: x + x, numbers) 
print(list(result)) 
>> {2, 4, 6, 8}
```

```
# List of strings 
l = ['sat', 'bat', 'cat', 'mat'] 

# map() can listify the list of strings individually 
test = list(map(list, l)) 
print(test) 
>> [['s', 'a', 't'], ['b', 'a', 't'], ['c', 'a', 't'], ['m', 'a', 't']]
```

39. What is reduce() in python?

The **reduce(fun,seq)** function is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along.This function is defined in “functools” module.

Working : 

- At first step, first two elements of sequence are picked and the result is obtained.
- Next step is to apply the same function to the previously attained result and the number just succeeding the second element and the result is again stored.
- This process continues till no more elements are left in the container.
- The final returned result is returned and printed on console.

```
# python code to demonstrate working of reduce() 

# importing functools for reduce() 
import functools 

# initializing list 
lis = [ 1 , 3, 5, 6, 2, ] 

# using reduce to compute sum of list 
print ("The sum of the list elements is : ",end="") 
print (functools.reduce(lambda a,b : a+b,lis)) 

# using reduce to compute maximum element from list 
print ("The maximum element of the list is : ",end="") 
>> The sum of the list elements is : 17
print (functools.reduce(lambda a,b : a if a > b else b,lis)) 
>> The maximum element of the list is : 6

```

40. one django application and want to run 2 different python version like 2 different node model

41. What are docstrings in Python?

- Docstrings are not actually comments, but, they are documentation strings. These docstrings are within triple quotes. They are not assigned to any variable and therefore, at times, serve the purpose of comments as well.

```
"""
Using docstring as a comment.
This code divides 2 numbers
"""
x=8
y=4
z=x/y
print(z)
>> 2.0
```

42. What is the purpose of is, not and in operators?

- Operators are special functions. They take one or more values and produce a corresponding result.

**is**: returns true when 2 operands are true  (Example: “a” is ‘a’)

**not**: returns the inverse of the boolean value

**in**: checks if some element is present in some sequence

43. What are the generators in python?

- Functions that return an iterable set of items are called generators.
- **Generator-Function** : A generator-function is defined like a normal function, but whenever it needs to generate a value, it does so with the yield keyword rather than return. If the body of a def contains yield, the function automatically becomes a generator function.

```
# A generator function that yields 1 for first time, 
# 2 second time and 3 third time 
def simpleGeneratorFun(): 
	yield 1			
	yield 2			
	yield 3			

# Driver code to check above generator function 
for value in simpleGeneratorFun(): 
	print(value) 

>> 1
>> 2
>> 3
```

- **Generator-Object** : Generator functions return a generator object. Generator objects are used either by calling the next method on the generator object or using the generator object in a “for in” loop (as shown in the above program).

```
# A Python program to demonstrate use of 
# generator object with next() 

# A generator function 
def simpleGeneratorFun(): 
	yield 1
	yield 2
	yield 3

# x is a generator object 
x = simpleGeneratorFun() 

# Iterating over the generator object using next 
print(x.next()); # In Python 3, __next__() 
print(x.next()); 
print(x.next()); 

>> 1
2
3
```

- Generator function returns an generator object that is iterable, i.e., can be used as an Iterators.

44. How will you capitalize the first letter of string?

- In Python, the capitalize() method capitalizes the first letter of a string. If the string already consists of a capital letter at the beginning, then, it returns the original string.

45. How will you convert a string to all lowercase or uppercase?

- To convert a string to lowercase, lower() function can be used and for uppercase, upper().

```
stg='ABCD'
print(stg.lower())
print(stg.upper())
```

46. What is the usage of help() and dir() function in Python?

- Help() and dir() both functions are accessible from the Python interpreter and used for viewing a consolidated dump of built-in functions. 

- **Help()** function: The help() function is used to display the documentation string and also facilitates you to see the help related to modules, keywords, attributes, etc.
- **Dir()** function: The dir() function is used to display the defined symbols.

```
>>> help(x)
Help on generator object:

sgf = class generator(object)
 |  Methods defined here:
 |
 |  __del__(...)
 |
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |
 |  __iter__(self, /)
 |      Implement iter(self).
 |
 |  __next__(self, /)
 |      Implement next(self).

>>> dir(x)
['__class__', '__del__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__name__', '__ne__', '__new__', '__next__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'close', 'gi_code', 'gi_frame', 'gi_running', 'gi_yieldfrom', 'send', 'throw']
```

47. Whenever Python exits, why isn’t all the memory de-allocated?

- Whenever Python exits, especially those Python modules which are having circular references to other objects or the objects that are referenced from the global namespaces are not always de-allocated or freed.
- It is impossible to de-allocate those portions of memory that are reserved by the C library.
- On exit, because of having its own efficient clean up mechanism, Python would try to de-allocate/destroy every other object.

48. What is a dictionary in Python?

- Dictionary in Python is an unordered collection of data values, used to store data values like a map, which unlike other Data Types that hold only single value as an element, Dictionary holds key:value pair. 
- Key value is provided in the dictionary to make it more optimized. 
- Each key-value pair in a Dictionary is separated by a colon :, whereas each key is separated by a ‘comma’.

```
dict={'Country':'India','Capital':'Delhi','PM':'Modi'}
print dict[Country]
>> India
print dict[Capital]
>> Delhi
print dict[PM]
>> Modi
```

49. What does this mean: ```*args```, ```**kwargs```? And why would we use it?

- The special syntax ```*args``` in function definitions in python is used to pass a variable number of arguments to a function. It is used to pass a non-keyworded, variable-length argument list.
```
arg = list or tuple
**kwargs = dic
```

```
# Python program to illustrate 
# *args for variable number of arguments 
def myFun(*argv): 
	for arg in argv: 
		print (arg) 
	
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks') 
```

- The special syntax ```**kwargs``` in function definitions in python is used to pass a keyworded, variable-length argument list. We use the name kwargs with the double star. The reason is because the double star allows us to pass through keyword arguments (and any number of them).

```
# Python program to illustrate 
# *kargs for variable number of keyword arguments 

def myFun(**kwargs): 
	for key, value in kwargs.items(): 
		print ("%s == %s" %(key, value)) 

# Driver code 
myFun(first ='Geeks', mid ='for', last='Geeks')	 
```

50. What does len() do?

- It is used to determine the length of a string, a list, an array, etc.

```
stg='ABCD'
len(stg)
>> 4
```

51. Explain split(), sub(), subn(), escape() methods of “re” module in Python.

- To modify the strings, Python’s “re” module is providing 3 methods. They are:

**split()** – Split string by the occurrences of a character or a pattern, upon finding that pattern, the remaining characters from the string are returned as part of the resulting list.
```
re.split(pattern, string, maxsplit=0, flags=0)
```

Example:
```
>>> a = "akash talole"
>>> a.split(' ')
['akash', 'talole']

# using re
>>> import re
>>> a = "akash,talole"
>>> re.split(',',a)
['akash', 'talole']
```

```
from re import split 

# '\W+' denotes Non-Alphanumeric Characters or group of characters 
# Upon finding ',' or whitespace ' ', the split(), splits the string from that point 
print(split('\W+', 'Words, words , Words')) 
print(split('\W+', "Word's words Words")) 

# Here ':', ' ' ,',' are not AlphaNumeric thus, the point where splitting occurs 
print(split('\W+', 'On 12th Jan 2016, at 11:02 AM')) 

# '\d+' denotes Numeric Characters or group of characters 
# Spliting occurs at '12', '2016', '11', '02' only 
print(split('\d+', 'On 12th Jan 2016, at 11:02 AM')) 

Output:
['Words', 'words', 'Words']
['Word', 's', 'words', 'Words']
['On', '12th', 'Jan', '2016', 'at', '11', '02', 'AM']
['On ', 'th Jan ', ', at ', ':', ' AM']
```

**sub()** – finds all substrings where the regex pattern matches and then replace them with a different string
```
re.sub(pattern, repl, string, count=0, flags=0)
```

**subn()** – it is similar to sub() and also returns the new string along with the no. of replacements.
```
re.subn(pattern, repl, string, count=0, flags=0)
```

**escape()** - Return string with all non-alphanumerics backslashed, this is useful if you want to match an arbitrary literal string that may have regular expression metacharacters in it.

52. What is unittest in Python?

- A unit testing framework in Python is known as unittest. It supports sharing of setups, automation testing, shutdown code for tests, aggregation of tests into collections etc.