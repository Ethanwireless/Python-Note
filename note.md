# Python Note

## Python Strings

### ord() and chr() Functions

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

### ```in```  and ```not in```  operators

You can use ```in``` and ```not in```  operators to check existence of string in another string. They are also known as membership operator.

```python
>>> s1 = "Welcome"
>>> "come" in s1
True
>>> "come" not in s1
False
```

### Testing strings

METHOD NAME	 | METHOD DESCRIPTION
------------- | --------------
isalnum() | Returns True if string is alphanumeric
isalpha() | Returns True if string contains only alphabets
isdigit() | Returns True if string contains only digits
isidentifier() |	Return True is string is valid identifier
islower()	| Returns True if string is in lowercase
isupper()	| Returns True if string is in uppercase
isspace()	| Returns True if string contains only whitespace

### Commonly used list methods with return type

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

### isinstance() function

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

### `re.search()` Method

`re.search()` is used to find the first match for the pattern in the string.

**Syntax:** `re.search(pattern, string, flags[optional])`

`re.search()` method accepts pattern and string and returns a `match object` on success or `None`  if no match is found. `match object`  has `group()`  method which contains the matching text in the string.

You must specify the pattern using **raw strings** i.e prepending string with r like this.

```python
r'this \n'.
```
example:

```python
>>> import re
>>> s = "my number is 123"
>>> match = re.search(r'\d\d\d', s)
>>> match
<_sre.SRE_Match object; span=(13, 16), match='123'>
>>> match.group()
'123'
```

### Basic patterns used in regular expression
SYMBOL | DESCRIPTION
--- | ---
. | dot matches any character except newline
\w | matches any word character i.e letters, alphanumeric, digits and underscore ( _ )
\W | matches non word characters
\d | matches a single digit
\D | matches a single character that is not a digit
\s | matches any white-spaces character like \n, \t, spaces
\S | matches single non white space character
[abc] | matches single character in the set i.e either match a, b or c
[\^abc] | match a single character other than a, b and c
[a-z] | match a single character in the range a to z.
[a-zA-Z] | match a single character in the range a-z or A-Z
[0-9] | match a single character in the range 0-9
^ | match start at beginning of the string
$ | match start at end of the string
\+ | matches one or more of the preceding character (greedy match).
\* | matches zero or more of the preceding character (greedy match).

example:

```python
import re
s = "tim email is tim@somehost.com"
match = re.search(r'[\w.-]+@[\w.-]+', s)
 
# the above regular expression will match a email address
 
if match:
    print(match.group())
else:
    print("match not found")
```

### Group capturing

```python
import re
s = "tim email is tim@somehost.com"
match = re.search('([\w.-]+)@([\w.-]+)', s)
if match:
    print(match.group()) ## tim@somehost.com (the whole match)
    print(match.group(1)) ## tim (the username, group 1)
    print(match.group(2)) ## somehost (the host, group 2)
```

## What is `if __name__ == “__main__”` ??
Every module in python has a special attribute called `__name__`. The value of `___name__`  attribute is set to `'__main__'`  when module run as main program. Otherwise the value of `__name__` is set to contain the name of the module.

## Python Lambda Function

```python
>>> r = lambda x, y: x * y
>>> r(12, 3)   # call the lambda function
36
```
or
`(lambda x, y: x * y)(3,4)`

## Python String Formatting

**Syntax:** `template.format(p1, p1, .... , k1=v1, k2=v2)`
**Syntax:** `{[argument_index_or_keyword]:[width][.precision][type]}`

`type`  can be used with format codes

FORMAT CODES | DESCRIPTION
--- | ---
d | for integers
f | for floating point numbers
b | for binary numbers
o | for octal numbers
x | for octal hexadecimal numbers
s | for string
e | for floating point in exponent format

example:

```python
>>> "Floating point {0:.2f}".format(345.7916732)
Floating point 345.79

>>> "In binary 4 is {0:b}".format(4) # b for binary
In binary 4 is 100

>>> array = [34, 66, 12]
>>> "A = {0}, B = {1}, C = {2}".format(*array)
'A = 34, B = 66, C = 12'

>>> d = {'hats' : 122, 'mats' : 42}
>>> "Sam had {hats} hats and {mats} mats".format(**d)
Sam had 122 hats and 42 mats

>>> 'Sam has {red} red balls, {green} yellow balls and {0} bats'.format(3, red = 12, green = 31)
Sam has 12 red balls, 31 yellow balls and 3 bats
```

## virtualenv

```sh
$ cd myproject/
$ virtualenv --no-site-packages venv
$ source venv/bin/activate
$ deactivate
```


