arr = [0, 3, 4, 2, 1]

*_, two, _ = arr
_, three, *_ = arr

_, b, *_, c, _ = arr
arr[1]

print(two)
print(three)

###

class Sos(type):

    def __lshift__(cls, other):
        print(str(other), end="")
        return cls

class cout(metaclass=Sos): pass

endl = '\n'

## Other file
# import std

cout << "Hello" << 4 << endl << "niceceee";

