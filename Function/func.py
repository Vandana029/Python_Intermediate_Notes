## Example 1
'''
def example(a, b=2, *args, **kwargs):
    print(a, b, args, kwargs)

example(1, 3, 4, 5, x=6, y=7)
# Output: 1 3 (4, 5) {'x': 6, 'y': 7}

## Example 2
x = 10
def f():
    global x
    x = 20
f()
print(x)  # 20 

## Example 3 (Mutable Default Argument)
'''
#Default mutable args persist across calls
'''
def append_list(val, lst=[]):
    lst.append(val)
    return lst

print(append_list(1))  # [1]
print(append_list(2))  # [1, 2], surprising behavior

# Fix
def append_list(val, lst=None):
    if lst is None:
        lst = []

## Example 3. Nested Functions & Closures
'''
#Inner function remembers variables even after outer function exits.
'''
def outer(x):
    def inner(y):
        return x + y
    return inner

f = outer(5)
print(f(3))  # 8 

## Example  4. Lambda Functions
'''
# Anonymous, single-expression functions.
# Late Binding: Captures last value of loop variable.
'''
add = lambda x, y: x + y
print(add(2, 3))  # 5

# Example of Late Binding
funcs = [lambda x=i: x for i in range(3)]
print([f() for f in funcs])  # [0, 1, 2]
# Correct way (capture value using default arg).



## Example 5. Decorators (Basic Intro)
'''
#Function that modifies another function.
'''
def decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@decorator
def say_hello():
    print("Hello")

say_hello()


## Example 6. Recursion using lambda
# Factorial using recursion with lambda
f = lambda x: 1 if x == 0  or x == 1 else x * f(x - 1)
print(f(5))  # 120


## Example 7. nonlocal Keyword
def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner

counter = outer()
print(counter())  # 1
print(counter())  # 2

## Explaination:
# outer() is called:
    # count = 0 is created in outer()'s scope.
    # inner() is defined — it can access count, and it uses nonlocal to modify it.
    # outer() returns inner() — but not executed yet, just returned.
# counter = outer():
    # Now counter refers to the inner() function, along with its closure (a reference to count = 0).
# First call counter():
    # Executes inner().
    # It sees nonlocal count, so it uses count from outer().
    # count += 1 → count becomes 1.
    # Returns 1.
# Second call counter():
    # Same inner() is run again.
    # This time, count is already 1.
    # count += 1 → count becomes 2.
    # Returns 2.


## Example 8. Closure
'''
# A closure happens when the inner function remembers the outer function’s variable even after the outer function is done.
# Real-Life Use: Data encapsulation, decorators, function factories.
'''
def multiplier(x):
    def multiply(y):
        return x * y  # x is "remembered" by multiply()
    return multiply

double = multiplier(2)
print(double(5))  # 10 
# Even though multiplier() has finished running, double() retains access to x = 2.
'''

