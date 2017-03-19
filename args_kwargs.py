# Python *args and **kwargs

# *args  allows us to pass variable number of arguments to the function.
def sum(*args):
    s = 0
    for i in args:
        s += i
    print("sum is", s)

# sum(1, 2, 3, 4, 5, 7)

# **kwargs allows us to pass variable number of keyword argument
def my_func(**kwargs):
    for i, j in kwargs.items():
        print(i, j)