def lshift(cls, other):
    print(other, end="")
    return cls

meat = type("",(type,),{"__lshift__" : lshift})

class cout(metaclass=meat): pass

endl = eval("(lambda : \'\n\')( )")

# base = type("", (), {
#     "__init_subclass__": lambda cls, **kwargs: None
# })

#cout = type("cout", (base), {})

input = """
cout << "hallo" << endl;
"""

compiler = exec
compiler(input)

# dict: {x: x ** 2 for x in range(10)}
# eval/exec

