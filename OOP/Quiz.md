# Question 1: Class vs Instance Variable
Q: What will be the output? Is `x` shared between instances?
```
class MyClass:
    x = []

    def __init__(self, val):
        self.x.append(val)

a = MyClass(1)
b = MyClass(2)
print(a.x)  
print(b.x)  
```
**Answer:**
```
[1, 2]
[1, 2]
```
- `x `is a class variable, shared among all instances.
- Both `a` and `b` share the same `x` list. So appending to it through any instance affects the shared list.

---

# Question 2: `super()` vs direct parent class call
Q: What’s the order of constructor calls? Why?
```
class A:
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
        super().__init__()
        print("B")

class C(A):
    def __init__(self):
        super().__init__()
        print("C")

class D(B, C):
    def __init__(self):
        super().__init__()
        print("D")

D()  
```
**Answer:**
```
A
C
B
D
```
- Python uses C3 linearization (MRO).
- `super()` follows MRO: D → B → C → A
- `super().__init__()` in each class calls the next in MRO.

---

# Question 3: Dunder Methods and Operator Overloading
Q 1: Why is `+` giving multiplication result? What's going on here?
```
class Number:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        return self.val * other.val

a = Number(2)
b = Number(3)
print(a + b)  
```
**Answer:**
Q1. Output: `6`. Why? -> `__add__` is overridden to return `self.val * other.val`.


Q 2: How is `+` overloaded here?
```
class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return Book(self.pages + other.pages)

b1 = Book(100)
b2 = Book(150)
print((b1 + b2).pages)
```
**Answer:**
Output: `250`
Why?
`__add__` returns a new Book instance with combined pages.

---

# Question 4: Method Overriding and MRO
Q: What will this print? Why does `super()` work this way?
```
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        print("Hello from Child")

def greet_twice(obj):
    obj.greet()
    super(Child, obj).greet()

greet_twice(Child())  
```
**Answer:**
```
Hello from Child
Hello from Parent
```
- `super(Child, obj)` tells Python: start searching after `Child` in the MRO.
- So it finds `Parent.greet`.

---

# Question 5: Encapsulation - Private Variables
Q: Will this throw an error? How can you access `__data`?
```
class Secret:
    def __init__(self):
        self.__data = "hidden"

obj = Secret()
print(obj.__data)  
```
**Answer:**
Error: `AttributeError: 'Secret' object has no attribute '__data'`

- `__data` gets name-mangled to `_Secret__data`.
- To access: `obj._Secret__data`

---

# Question 6: Custom `__str__` and` __repr__`
Q: Why are outputs different in each print?
```
class Demo:
    def __str__(self):
        return "str"

    def __repr__(self):
        return "repr"

d = Demo()
print(d)
print([d])  
```
**Answer:**
```
print(d)     → str
print([d])   → [repr]
```
- `print(d)` calls `__str__`.
- `print([d])` uses `__repr__` to represent the object inside the list.

---

# Question 7: Static vs Class Methods
Q: What's the difference in behavior? When would you use each?
```
class Sample:
    @staticmethod
    def foo():
        print("Static")

    @classmethod
    def bar(cls):
        print("Class", cls)

Sample.foo()
Sample.bar()
```
**Answer:**
```
Sample.foo()  → Static
Sample.bar()  → Class <class '__main__.Sample'>
```
- `@staticmethod`: no `self` or `cls`, behaves like a plain function.
- `@classmethod`: receives `cls`, knows class context.

---

# Question 8: Metaclass Logic
Q: What is a metaclass? What is printed and when? When and why is `__new__` of metaclass called?
```
class Meta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name}")
        return super().__new__(cls, name, bases, dct)

class Test(metaclass=Meta):
    pass  
```
**Answer:**
Output: `Creating class Test`
- `__new__` of metaclass is called **when the class is defined**, not when an instance is created.

---

# Question 11: Overriding `__eq__` and Using in Set
Q: Why is the output surprising? How to fix it?
```
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

p1 = Point(1, 2)
p2 = Point(1, 2)
s = {p1, p2}
print(len(s))
```
**Answer:**
Output: `2`
- Set uses `__hash__` for uniqueness.
- here, we overrode __eq__ but not __hash__, so objects are treated as distinct.
- Fix: add
```
def __hash__(self):
    return hash((self.x, self.y))
```

---

# Question 12: Mutable Default Arguments in Methods
Q. What's printed? Why?
```
class MyClass:
    def __init__(self, data=[]):
        self.data = data

a = MyClass()
a.data.append(1)

b = MyClass()
print(b.data)
```
**Answer:**
`print(b.data)  → [1]`
- `data=[]` is evaluated once. Shared across instances unless explicitly overridden.

---

# Question 13: Private vs Protected vs Name Mangling
Q. Which lines fail and why?
```
class Demo:
    def __init__(self):
        self._protected = "protected"
        self.__private = "private"

obj = Demo()
print(obj._protected) # OK
print(obj.__private) # ERROR
```
**Answer:**
- `_protected`: just a convention.
- `__private`: name-mangled to `_Demo__private`.

---

# Question 14: Class vs Instance Attribute Conflict
Q. Why are outputs different?
```
class Test:
    x = 10

t1 = Test()
t2 = Test()
t1.x = 20

print(t1.x)
print(t2.x)
print(Test.x)
```
**Answer:**
- `t1.x = 20` -> Creates instance variable x on t1. It shadows class variable.
```
t1.x → 20
t2.x → 10
Test.x → 10
```

---

# Question 15: Property Decorator
Q. How is validation handled here?
```
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = max(0, value)

c = Circle(5)
c.radius = -10
print(c.radius)
```
**Answer:**
- Setter ensures radius is non-negative using `max(0, value)`.
- @property gives controlled access.

