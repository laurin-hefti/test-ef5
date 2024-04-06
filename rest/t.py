class M(type):
    def __prepare__(name, *bases, **kwargs):
        print(name)
        print(bases)
        print(kwargs)
        return dict()

@dec
class B(metaclass=M, hh="lkdj"):

    def __prepare__(name, *bases, **kwargs):
        pass


def dec(arg):
    def d(): pass

    return d



