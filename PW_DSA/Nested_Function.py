def func1():
    print("This is Outer Function")
    def func2():
        print("This is Inner Function")
    return func2


func1()()

def outer():
    print("outer")
    def inner():
        print("Hello Supreme")
    return inner
outer()()