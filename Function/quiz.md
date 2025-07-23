# 1. Mutable Default Argument Trap
Q. What is the output and why?
```
def append_to_list(val, lst=[]):
    lst.append(val)
    return lst

print(append_to_list(1))  # ?
print(append_to_list(2))  # ?
print(append_to_list(3))  # ?
```
**Ans**:
```
[1]
[1, 2]
[1, 2, 3]
```
**Explanation**: 
- Default (mutable) arguments are evaluated only once at function definition time.
- So the default list `lst` is shared across all calls to `append_to_list()` where no new list is provided.
- Every time you call `append_to_list()` without passing `lst`, it appends to the same list.
**Best Practice**: Avoid mutable default arguments. Use `None` and then set it inside:
```
def func(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
```

**One More Example**:
```
def func(a, L=[]):
    L.append(a)
    return L

print(func(1))
print(func(2))
print(func(5, ['a', 'b']))
print(func(3))

# Output:
[1]
[1, 2]
['a', 'b', 5]
[1, 2, 3]
```

---

# 2. Keyword vs Positional Arguments
Q. Which line throws an error and why?
```
def func(a, b=2, c=3):
    print(a, b, c)

func(1)           # A  
func(1, c=5)      # B  
func(a=1, 4)      # C 
```
**Ans:**
Line C throws an error.
**Explanation:**
`func(a=1, 4)` → Invalid syntax: positional arguments can't follow keyword arguments.

---

# 3. Late Binding in Lambda
Q. What will this print and why?
```
funcs = [lambda: i for i in range(4)]
results = [f() for f in funcs]
print(results)
```
**Ans:**
`[3, 3, 3, 3]`
It is equivalent to below code:
```
funcs = []
for i in range(4):
    funcs.append(lambda: i)

print([f() for f in funcs])
```
**Explanation:**
- Lambdas capture the variable *by reference*, not by value.
- When the lambda is finally executed, it uses the *current* value of `i`, which is `3` after the loop ends.
**Fix using default argument (early binding):**
```
funcs = []
for i in range(4):
    funcs.append(lambda i=i: i)  # Now `i` is captured by value

print([f() for f in funcs])  # [0, 1, 2, 3]
```
**OR**
```
funcs = [lambda i=i: i for i in range(4)]
results = [f() for f in funcs]
print(results)
```

---

# 4. nonlocal Behavior Test
Q. Does this work? If not, what fix is needed?
```
def make_counter():
    count = 0
    def counter():
        count += 1
        return count
    return counter

c = make_counter()
print(c())  # ?
```
**Ans**: It will give `UnboundLocalError: cannot access local variable 'count' where it is not associated with a value`. To make it work, we need to add `nonlocal` in front of `count` inside `counter()` function.

---

# 5. Closure State Preservation
Q Does the `x = 20` outside affect the output? Why or why not?
```
def outer():
    x = 10
    def inner():
        return x
    return inner

fn = outer()
print(fn())     # A
x = 20
print(fn())     # B
```
**Ans:**
```
A → 10  
B → 10
```
**Explanation:**
- `outer()` creates a closure: `inner()` captures the enclosed variable `x = 10` from its scope.
- The outer `x = 20` in global scope does not affect the inner function.
- `inner()` uses the `x` it closed over during the call to `outer()`.
- **Closure keeps a snapshot of the variables in its enclosing scope.**

---

# 6. Variable Scope Shadowing
Q. Does this print 5 and 10? If not, what error do you get?
```
x = 5

def foo():
    print(x) # A
    x = 10
    print(x)

foo()
```
**Ans:**
`UnboundLocalError: cannot access local variable 'x' where it is not associated with a value` at 'A'.
**Explanation:**
- Python thinks `x` is a local variable because we assign to it in the function.
- So when we try to `print(x)` before assignment, it crashes.
- If you want to use the global `x`, use `global x` at the top of the function.

---

# 7. Function Argument Unpacking 
Q. Is this valid? What happens?
```
def f(a, b, c):
    print(a, b, c)

args = [1, 2]
f(*args, 3)  # ?
```
**Ans:**
Valid. Output is:
`1 2 3`
**Explanation:**
- `*args` unpacks into positional arguments.
- `f(*args, 3)` becomes `f(1, 2, 3)` internally.
- **NOTE:** You can mix unpacked and regular values as long as the final argument count matches the function signature.

---

# 8. Decorator Output Test
Q. What will be the printed output?
```
def decorator(f):
    def wrapper(*args):
        print("Before")
        result = f(*args)
        print("After")
        return result
    return wrapper

@decorator
def greet(name):
    print("Hello", name)

greet("Alice")
```
**Answer:**
```
Before  
Hello Alice  
After
```
**Explanation:**
- `@decorator` wraps `greet()` with `wrapper()`.

---
 
# 9. Function Overwriting
Q. Does this work? Why or why not?
```
def greet():
    print("Hello")

greet = 5
greet()
```
**Ans:**
Error – `TypeError: 'int' object is not callable`
**Explanation:**
- After `greet = 5`, the original function is overwritten.
- Now, `greet()` tries to call an integer, which is not callable

---

# 10. Function with *args and **kwargs
Q. What’s printed? Explain the grouping
```
def f(a, *args, **kwargs):
    print(a, args, kwargs)

f(1, 2, 3, x=10, y=20)
```
**Ans:**
`1 (2, 3) {'x': 10, 'y': 20}`
**Explanation:**
- `*args` collects extra positional arguments.
- `**kwargs` collects extra keyword arguments.

---

# 11. Will this run? What does it print?
```
def foo():
    print(bar())

def bar():
    return "Hello"

foo()
```
**Ans:**
`Hello`
**Explanation**:
- Even though `bar()` is defined after `foo()`, Python allows this because `bar()` is only *called* when `foo()` is executed, not during function definition.
- Python's parser builds the function definitions first and resolves the names at runtime.