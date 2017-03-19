#Python Note

## Python Strings

#### ord() and chr() Functions

**ord()** – function returns the ASCII code of the character.
**chr()** – function returns character represented by a ASCII number.

```python
>>> ch = 'b'
>>> ord(ch)
98
>>> chr(97)
'a'
>>> ord('A')
65
```

#### ```in```  and ```not in```  operators

You can use ```in``` and ```not in```  operators to check existence of string in another string. They are also known as membership operator.

```python
>>> s1 = "Welcome"
>>> "come" in s1
True
>>> "come" not in s1
False
```

#### Testing strings

METHOD NAME	 | METHOD DESCRIPTION
------------- | --------------
isalnum() | Returns True if string is alphanumeric
isalpha() | Returns True if string contains only alphabets
isdigit() | Returns True if string contains only digits
isidentifier() |	Return True is string is valid identifier
islower()	| Returns True if string is in lowercase
isupper()	| Returns True if string is in uppercase
isspace()	| Returns True if string contains only whitespace

#### Commonly used list methods with return type

METHOD | NAME	DESCRIPTION
---|---
count(x:object):int | Returns the number of times element x appears in the list.
extend(l:list):None	| Appends all the elements in l  to the list and returns None.
index(x: object):int |	Returns the index of the first occurrence of element x in the list
insert(index: int, x: object):None | Inserts an element x at a given index. Note that the first element in the list has index 0 and returns None..
remove(x:object):None |	Removes the first occurrence of element x from the list and returns None
reverse():None | Reverse the list and returns None
sort(): None | Sorts the elements in the list in ascending order and returns None.
pop(i): object | Removes the element at the given position and returns it. The parameter i is optional. If it is not specified, pop() removes and returns the last element in the list.

## Python Tuples

In Python Tuples are very similar to list but once a tuple is created, you cannot add, delete, replace, reorder elements.

```python
>>> t1 = () # creates an empty tuple with no data
>>> t2 = (11,22,33)
>>> t3 = tuple([1,2,3,4,4]) # tuple from array
>>> t4 = tuple("abc") # tuple from string
```

## Python Operator Overloading

```python
import math
class Circle:
    def __init__(self, radius):
        self.__radius = radius
    def setRadius(self, radius):
        self.__radius = radius
    def getRadius(self):
        return self.__radius
    def area(self):
        return math.pi * self.__radius ** 2
    def __add__(self, another_circle):
        return Circle( self.__radius + another_circle.__radius )
    def __gt__(self, another_circle):
        return self.__radius > another_circle.__radius
    def __lt__(self, another_circle):
        return self.__radius < another_circle.__radius
    def __str__(self):
        return "Circle with radius " + str(self.__radius)
 
c1 = Circle(4)
print(c1.getRadius())
 
c2 = Circle(5)
print(c2.getRadius())
 
c3 = c1 + c2
print(c3.getRadius())
 
print(c3 > c2) # Became possible because we have added __gt__ method
 
print(c1 < c2) # Became possible because we have added __lt__ method
 
print(c3) # Became possible because we have added __str__ method
```
Expected Output:

```python
4
5
9
True
True
Circle with radius 9
```

## Python inheritance and polymorphism

code ```super()``` method in derived class is used to call method of the base class

####isinstance() function

`isinstance()`  function is used to determine whether the object is an instance of the class or not.
**Syntax:** `isinstance(object, class_type)`

## Python Exception Handling

```python
try:
    <body>
except <ExceptionType1>:
    <handler1>
except <ExceptionTypeN>:
    <handlerN>
except:
    <handlerExcept>
else:
    <process_else>
finally:
    <process_finally>
```
`except` clause is similar to `elif`. When exception occurs, it is checked to match the exception type in `except` clause. If match is found then handler for the matching case is executed. Also note that in last `except` clause `ExceptionType` is omitted. If exception does not match any exception type before the last `except` clause, then the handler for last `except` clause is executed.

## Python *args and **kwargs

`*args`  allows us to pass variable number of arguments to the function. Let’s take an example to make this clear.

`**kwargs` allows us to pass variable number of keyword argument like this
`func_name(name='tim', team='school')`

```python
my_func(name='tim', sport='football', roll=19)

def my_three(a, b, c):
    print(a, b, c)
 
a = [1,2,3]
my_three(*a) # here list is broken into three elements
```

```python
def my_three(a, b, c):
    print(a, b, c)
 
a = {'a': "one", 'b': "two", 'c': "three" }
my_three(**a)
```

## Python Regular Expression



