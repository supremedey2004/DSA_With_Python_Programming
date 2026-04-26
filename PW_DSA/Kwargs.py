# def student_info(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
#
# student_info(name="Supreme", age=20, branch="CSE")

def demo(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

demo(1, 2, 3, "Supreme", 20)