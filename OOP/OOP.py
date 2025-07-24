class Test:
    x = 10
    def f1():
        m1 = 4
    def __init__(self, a):
        self.a = a

t1 = Test(3)
t2 = Test(5)

# All variable names in above code
# x, m1, a, t1.a, t2.a, f1, __init__, Test, self
# x = class object variable
# m1 = local variable
# a = local variabl
# t1.a = Instance object variable
# t2.a = Instance object variable
# t1 = global variable
# t2 = global variable
# self = local variable
# Test = global variable
# f1 = variable to represent function object
# __init__ = variable to represent function object

#################################################################################

class Test2:
    x1 = 5 # class object variable (or static variable)

    # Instance method (because of 'self' argument)
    def f1(self):   
        self.a = 10
        Test2.x2 = 30

    @staticmethod
    def f2():
        print('Hello!')
        Test2.x3 = 24
         
    @classmethod
    def f3(cls):
        cls.x=5
        Test2.x5 = 29

def fun():
    print('Non member function')

t1 = Test2()
t1.b = 15
print(t1.b) # 15
t1.f1() # Instance Method. This is same as f1(t1), t1 is being passed implicitly to f1().
Test2.x4 = 9

Test2.f2() # Static Method. simply calls f2().
Test2.f3() # Class Method. This is same as f3(Test2), Test2 is being passed implicitly to f3().