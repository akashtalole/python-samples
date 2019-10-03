## Python Concepts

[DevOps](devops.md)

[k8s](k8s.md)

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


=======================================================================================

53. What is conda?

- Package, dependency and environment management for any language—Python, R, Ruby, Lua, Scala, Java, JavaScript, C/ C++, FORTRAN, and more.

- Conda is an open source package management system and environment management system that runs on Windows, macOS and Linux. Conda quickly installs, runs and updates packages and their dependencies. 
- Conda easily creates, saves, loads and switches between environments on your local computer. It was created for Python programs, but it can package and distribute software for any language.

- Conda as a package manager helps you find and install packages. 
- If you need a package that requires a different version of Python, you do not need to switch to a different environment manager, because conda is also an environment manager. With just a few commands, you can set up a totally separate environment to run that different version of Python, while continuing to run your usual version of Python in your normal environment.

54. What is numpy?

- NumPy is the fundamental package for scientific computing with Python. It mostly used for solving matrix problems.
- Creating a Numpy Array:
```
>>> import numpy as np
>>> arr = np.array([])
>>> type(arr)
numpy.ndarray
```

55. What is pandas?

- Pandas is the most popular machine learning library written in python, for data manipulation and analysis.
- Creating a Series: A Series is a one dimensional labeled array like object.
```
>>> pd.Series([1,2,3,4,5])
0    1
1    2
2    3
3    4
4    5
dtype: int64
```

56. What is scikit-learn?

- Matplotlib, a great library for Data Visualization

```
import matplotlib.pyplot as plt
%matplotlib inline

dataset = pd.read_csv("../dataset/student_result.csv")

# This line will shows the result distribution
# result attribute contains two types of value. 
# 1 indicates `pass` and `0` indicates `fail`
dataset.result.value_counts().plot.bar() 
```

57. What is matplotlib?

- A library that provides a range of Supervised and Unsupervised Learning Algorithms. This library mainly focused on model building.
```
import numpy as np 
import pandas as pd

# 4 Supervised Classification Learning Algorithms
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

>>> dataset = pd.read_csv(r"../dataset/student_result.csv")
>>> print(dataset.head())

   math  bangla  english  result
0    70      80       90       1
1    30      40       50       0
2    50      20       35       0
3    80      33       33       1
4    33      35       36       1
```

58. What is NLTK?

- Natural Language Toolkit (NLTK) is a library for NLP (Natural Langue Processing).
- According to techopedia, Tokenization is the act of breaking up a sequence of strings into pieces such as words, keywords, phrases, symbols and other elements called tokens.

```
>>> from nltk.tokenize import word_tokenize
>>> sentence = "Hello! My Name is Nasir Islam Sujan."

# word_tokenize method will split the sentence into many token/pieces. 
>>> word_tokenize(sentence)
['Hello', '!', 'My', 'Name', 'is', 'Nasir', 'Islam', 'Sujan', '.']
```


# Kubernetes

- The Kubernetes Master is a collection of three processes that run on a single node in your cluster, which is designated as the master node. Those processes are: 
- kube-apiserver
- kube-controller-manager
- kube-scheduler.

- Each individual non-master node in your cluster runs two processes:
- kubelet, which communicates with the Kubernetes Master.
- kube-proxy, a network proxy which reflects Kubernetes networking services on each node.

- Kubernetes Objects
- The basic Kubernetes objects include:

- Pod
- Service
- Volume
- Namespace

- In addition, Kubernetes contains a number of higher-level abstractions called Controllers. Controllers build upon the basic objects, and provide additional functionality and convenience features. They include:

- ReplicaSet
- Deployment
- StatefulSet
- DaemonSet
- Job


1. How is Kubernetes related to Docker?

- It’s a known fact that Docker provides the lifecycle management of containers and a Docker image builds the runtime containers. 
- But, since these individual containers have to communicate, Kubernetes is used.  So, Docker builds the containers and these containers communicate with each other via Kubernetes. 
- So, containers running on multiple hosts can be manually linked and orchestrated using Kubernetes.

2. What is Container Orchestration?

- Consider a scenario where you have 5-6 microservices for an application. Now, these microservices are put in individual containers, but won’t be able to communicate without container orchestration. 
- So, as orchestration means the amalgamation of all instruments playing together in harmony in music, similarly container orchestration means all the services in individual containers working together to fulfill the needs of a single server.

3. What is the need for Container Orchestration?

- Consider you have 5-6 microservices for a single application performing various tasks, and all these microservices are put inside containers. Now, to make sure that these containers communicate with each other we need container orchestration.


# IoT

1. What are the main parts of IoT systems?

- IoT system consists of three main parts:

Sensors
Network connectivity
Data storage applications.

- What are security concerns related to IoT?

- This is the common IoT Interview Questions asked in an interview. Data security and privacy are major concerns related to IoT. These devices are vulnerable to hacking and cloud endpoints could be used by hackers to attack servers. Software developers and device designers have to ensure adequate security and privacy measures.

# Python Object Oriented Programming(OOP)

Python is a multi-paradigm programming language. Meaning, it supports different programming approach.

One of the popular approach to solve a programming problem is by creating objects. This is known as Object-Oriented Programming (OOP).

An object has two characteristics:

attributes
behavior
Let's take an example:

Parrot is an object,

name, age, color are attributes
singing, dancing are behavior
The concept of OOP in Python focuses on creating reusable code. This concept is also known as DRY (Don't Repeat Yourself).

In Python, the concept of OOP follows some basic principles:

- Inheritance	A process of using details from a new class without modifying existing class.
- Encapsulation	Hiding the private details of a class from other objects.
- Polymorphism	A concept of using common operation in different ways for different data input.

- Class
A class is a blueprint for the object.

We can think of class as an sketch of a parrot with labels. It contains all the details about the name, colors, size etc. Based on these descriptions, we can study about the parrot. Here, parrot is an object.

The example for class of parrot can be :
```
class Parrot:
    pass
```
Here, we use class keyword to define an empty class Parrot. From class, we construct instances. An instance is a specific object created from a particular class.

- Object
An object (instance) is an instantiation of a class. When class is defined, only the description for the object is defined. Therefore, no memory or storage is allocated.

The example for object of parrot class can be:
```
obj = Parrot()
```
Here, obj is object of class Parrot.

Suppose we have details of parrot. Now, we are going to show how to build the class and objects of parrot.
```
class Parrot:

    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

# instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# access the class attributes
print("Blu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))

# access the instance attributes
print("{} is {} years old".format( blu.name, blu.age))
print("{} is {} years old".format( woo.name, woo.age))
```

- Methods
Methods are functions defined inside the body of a class. They are used to define the behaviors of an object.
```
class Parrot:
    
    # instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # instance method
    def sing(self, song):
        return "{} sings {}".format(self.name, song)

    def dance(self):
        return "{} is now dancing".format(self.name)

# instantiate the object
blu = Parrot("Blu", 10)

# call our instance methods
print(blu.sing("'Happy'"))
print(blu.dance())
```

- Inheritance
Inheritance is a way of creating new class for using details of existing class without modifying it. The newly formed class is a derived class (or child class). Similarly, the existing class is a base class (or parent class).

```
# parent class
class Bird:
    
    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

# child class
class Penguin(Bird):

    def __init__(self):
        # call super() function
        super().__init__()
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")

peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()
```

- Encapsulation
Using OOP in Python, we can restrict access to methods and variables. This prevent data from direct modification which is called encapsulation. In Python, we denote private attribute using underscore as prefix i.e single "_ "or double "__".

```
class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()
```

- Polymorphism
Polymorphism is an ability (in OOP) to use common interface for multiple form (data types).

Suppose, we need to color a shape, there are multiple shape option (rectangle, square, circle). However we could use same method to color any shape. This concept is called Polymorphism.

```
class Parrot:

    def fly(self):
        print("Parrot can fly")
    
    def swim(self):
        print("Parrot can't swim")

class Penguin:

    def fly(self):
        print("Penguin can't fly")
    
    def swim(self):
        print("Penguin can swim")

# common interface
def flying_test(bird):
    bird.fly()

#instantiate objects
blu = Parrot()
peggy = Penguin()

# passing the object
flying_test(blu)
flying_test(peggy)
```

# Python Django Commands

```
django-admin startproject skyproj
python manage.py runserver 0.0.0.0:8000
python manage.py startapp myapp
#add model in myapp
#add app in project setting
python mange.py showmigrations
python mange.py makemigrations
python manage.py migrate
#add management commad in app/management/commands
python mange.py my_manage_command
python manage.py createsuperuser
python manage.py shell
```

1) Explain what is Django?

Django is a web framework in python to develop a web application in python.

2) Mention what are the features available in Django?

Features available in Django are

Admin Interface (CRUD)
Templating
Form handling
Internationalization
Session, user management, role-based permissions
Object-relational mapping (ORM)
Testing Framework
Fantastic Documentation
3) Mention the architecture of Django architecture?

Django architecture consists of

Models: It describes your database schema and your data structure
Views: It controls what a user sees, the view retrieves data from appropriate models and execute any calculation made to the data and pass it to the template
Templates: It determines how the user sees it. It describes how the data received from the views should be changed or formatted for display on the page
Controller: The Django framework and URL parsing
4) Why Django should be used for web-development?

It allows you to divide code modules into logical groups to make it flexible to change
To ease the website administration, it provides auto-generated web admin
It provides pre-packaged API for common user tasks
It gives you template system to define HTML template for your web page to avoid code duplication
It enables you to define what URL be for a given function
It enables you to separate business logic from the HTML
Everything is in python
5) Explain how you can create a project in Django?

To start a project in Django, you use command $ django-admin.py and then use the command

Project

_init_.py

manage.py

settings.py

urls.py

6) Explain how you can set up the Database in Django?

You can use the command edit mysite/setting.py , it is a normal python module with module level representing Django settings.

Django uses SQLite by default; it is easy for Django users as such it won’t require any other type of installation. In the case your database choice is different that you have to the following keys in the DATABASE ‘default’ item to match your database connection settings

Engines: you can change database by using ‘django.db.backends.sqlite3’ , ‘django.db.backeneds.mysql’, ‘django.db.backends.postgresql_psycopg2’, ‘django.db.backends.oracle’ and so on
Name: The name of your database. In the case if you are using SQLite as your database, in that case database will be a file on your computer, Name should be a full absolute path, including file name of that file.
If you are not choosing SQLite as your database then setting like Password, Host, User, etc. must be added.

7) Give an example how you can write a VIEW in Django?

Views are Django functions that take a request and return a response.  To write a view in Django we take a simple example of “Guru99_home” which uses the template Guru99_home.html and uses the date-time module to tell us what the time is whenever the page is refreshed.  The file we required to edit is called view.py, and it will be inside mysite/myapp/

Copy the below code into it and save the file

       from datatime import datetime

      from django.shortcuts import render

     def home (request):

              return render(request, ‘Guru99_home.html’, {‘right_now’: datetime.utcnow()})

Once you have determined the VIEW, you can uncomment this line in urls.py

# url ( r ‘^$’ , ‘mysite.myapp.views.home’ , name ‘Guru99’),

The last step will reload your web app so that the changes are noticed by the web server.

8) Explain how you can setup static files in Django?

There are three main things required to set up static files in Django

Set STATIC_ROOT in settings.py
run manage.py collectsatic
set up a Static Files entry on the PythonAnywhere web tab
9) Mention what does the Django templates consists of?

The template is a simple text file.  It can create any text-based format like XML, CSV, HTML, etc.  A template contains variables that get replaced with values when the template is evaluated and tags (% tag %) that controls the logic of the template.

10) Explain the use of session framework in Django?

In Django, the session framework enables you to store and retrieve arbitrary data on a per-site-visitor basis.  It stores data on the server side and abstracts the receiving and sending of cookies.  Session can be implemented through a piece of middleware.

11) Explain how you can use file based sessions?

To use file based session you have to set the SESSION_ENGINE settings to “django.contrib.sessions.backends.file”

12) Explain the migration in Django and how you can do in SQL?

Migration in Django is to make changes to your models like deleting a model, adding a field, etc. into your database schema.  There are several commands you use to interact with migrations.

Migrate
Makemigrations
Sqlmigrate
To do the migration in SQL, you have to print the SQL statement for resetting sequences for a given app name.

django-admin.py sqlsequencreset

Use this command to generate SQL that will fix cases where a sequence is out sync with its automatically incremented field data.

13) Mention what command line can be used to load data into Django?

To load data into Django you have to use the command line Django-admin.py loaddata. The command line will searches the data and loads the contents of the named fixtures into the database.

14) Explain what does django-admin.py makemessages command is used for?

This command line executes over the entire source tree of the current directory and abstracts all the strings marked for translation.  It makes a message file in the locale directory.

15) List out the inheritance styles in Django?

In Django, there is three possible inheritance styles

Abstract base classes: This style is used when you only wants parent’s class to hold information that you don’t want to type out for each child model
Multi-table Inheritance: This style is used If you are sub-classing an existing model and need each model to have its own database table
Proxy models: You can use this model, If you only want to modify the Python level behavior of the model, without changing the model’s fields
16) Mention what does the Django field class types?

Field class types determines

The database column type
The default HTML widget to avail while rendering a form field
The minimal validation requirements used in Django admin and in automatically generated forms


# Python: An Intro to caching

- A cache is a way to store a limited amount of data such that future requests for said data can be retrieved faster. In this article, we’ll look at a simple example that uses a dictionary for our cache. Then we’ll move on to using the Python standard library’s functools module to create a cache. 
- Let’s start by creating a class that will construct our cache dictionary and then we’ll extend it as necessary.

```
class MyCache:
    
    def __init__(self):
        """Constructor"""
        self.cache = {}
        self.max_cache_size = 10
```

There’s nothing in particular that’s special in this class example. We just create a simple class and set up two class variables or properties, cache and max_cache_size. The cache is just an empty dictionary while the other is self-explanatory. Let’s flesh this code out and make it actually do something:

```
import datetime
import random
 
class MyCache:
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        self.cache = {}
        self.max_cache_size = 10
 
    #----------------------------------------------------------------------
    def __contains__(self, key):
        """
        Returns True or False depending on whether or not the key is in the 
        cache
        """
        return key in self.cache
 
    #----------------------------------------------------------------------
    def update(self, key, value):
        """
        Update the cache dictionary and optionally remove the oldest item
        """
        if key not in self.cache and len(self.cache) >= self.max_cache_size:
            self.remove_oldest()
 
        self.cache[key] = {'date_accessed': datetime.datetime.now(),
                           'value': value}
 
    #----------------------------------------------------------------------
    def remove_oldest(self):
        """
        Remove the entry that has the oldest accessed date
        """
        oldest_entry = None
        for key in self.cache:
            if oldest_entry is None:
                oldest_entry = key
            elif self.cache[key]['date_accessed'] < self.cache[oldest_entry][
                'date_accessed']:
                oldest_entry = key
        self.cache.pop(oldest_entry)
 
    #----------------------------------------------------------------------
    @property
    def size(self):
        """
        Return the size of the cache
        """
        return len(self.cache)
```

- Here we import the datetime and random modules and then we see the class we created earlier. This time around, we add a few methods. One of the methods is a magic method called __contains__. I’m abusing it a little, but the basic idea is that it will allow us to check the class instance to see if it contains the key we’re looking for. The update method will update our cache dictionary with the new key / value pair. It will also remove the oldest entry if the maximum cache value is reached or exceeded. The remove_oldest method actually does the removing of the oldest entry in the dictionary, which in this case means the item that has the oldest access date. Finally we have a property called size which returns the size of our cache.

If you add the following code, we can test that the cache works as expected:

```
if __name__ == '__main__':
    # Test the cache
    keys = ['test', 'red', 'fox', 'fence', 'junk',
            'other', 'alpha', 'bravo', 'cal', 'devo',
            'ele']
    s = 'abcdefghijklmnop'
    cache = MyCache()
    for i, key in enumerate(keys):
        if key in cache:
            continue
        else:
            value = ''.join([random.choice(s) for i in range(20)])
            cache.update(key, value)
        print("#%s iterations, #%s cached entries" % (i+1, cache.size))
    print
```

- In this example, we set up a bunch of predefined keys and loop over them. We add keys to the cache if they don’t already exist. The piece missing is a way to update the date accessed, but I’ll leave that as an exercise for the reader. If you run this code, you’ll notice that when the cache fills up, it starts deleting the old entries appropriately.
- Now let’s move on and take a look at another way of creating caches using Python’s built-in functools module!

- The model layer¶
Django provides an abstraction layer (the “models”) for structuring and manipulating the data of your Web application.

- The view layer¶
Django has the concept of “views” to encapsulate the logic responsible for processing a user’s request and for returning the response.

- The template layer¶
The template layer provides a designer-friendly syntax for rendering the information to be presented to the user.


# Apache Kafka

- Apache Kafka is a real-time streaming platform that is gaining broad adoption within large and small organizations. 
-Kafka’s distributed microservices architecture and publish/subscribe protocol make it ideal for moving real-time data between enterprise systems and applications.

- Use cases
Messaging. Kafka works well as a replacement for a more traditional message broker
Website Activity Tracking. The original use case for Kafka was to be able to rebuild a user activity tracking pipeline as a set of real-time publish-subscribe feeds.
Metrics
Log Aggregation
Stream Processing
Event Sourcing
Commit Log.