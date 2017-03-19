# Python Strings

## ord() and chr() Functions

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

## ```in```  and ```not in```  operators
You can use ```in``` and ```not in```  operators to check existence of string in another string. They are also known as membership operator.

```python
>>> s1 = "Welcome"
>>> "come" in s1
True
>>> "come" not in s1
False
```

## Testing strings
METHOD NAME	 | METHOD DESCRIPTION
------------- | --------------
isalnum() | Returns True if string is alphanumeric
isalpha() | Returns True if string contains only alphabets
isdigit() | Returns True if string contains only digits
isidentifier() |	Return True is string is valid identifier
islower()	| Returns True if string is in lowercase
isupper()	| Returns True if string is in uppercase
isspace()	| Returns True if string contains only whitespace

## Commonly used list methods with return type

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


