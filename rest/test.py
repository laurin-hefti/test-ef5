from typing import Any


class F:
    def f(self):
        return 1
    
    def f(self, arg1):
        return 2


F2 = type(
    "F2",
    (),
    {
        "f": lambda s, arg1: 2,
    }
)

ff = F2()
ff.f(8)
# ff.f()

def int_init(s, x):
    print(x)
    s.val = x

# int = type(
#     "int",
#     (int,),
#     {
#         "__init__" : int_init,
#         "__add__": lambda x, y: x**y,
#     }
# )
# a = int(8+2)
# b = a + 2
# print(a)

def double(s, name, x):
    s.__dict__[name] = x * 3
    print("heello")

def hoi(s):
    print("moin")

def own_getr(s, name):
    print("getr")

class TMeat(type):
    def __new__(cls, name, bases, dct):
        print(name)
        dct = {
            "hello": hoi,
            **dct,
            "__getattr__": own_getr,
            "__setattr__": double,
        }
        x = type(name, bases, dct)
        # x.x = 6
        print("New")
        return x
    
    def __call__(self, *args):
        print("called")
        return self
    
    # def __setattr__(self, __name: str, __value: Any) -> None:
    #     pass

class T(metaclass=TMeat):
    x = 5

# Meta class functions:
#   define how the CLASS is handled, constructed etc
#
# Normal classes define only the construction of instances

t = T()
# t.x = 3
print(t.x)
t.hello()