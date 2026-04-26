def func(*args):
    print(type(args))
    print(args)
    sum=0
    for x in args:
        sum=sum+x
    return sum

print(func(10,20,40,70,50,80,))