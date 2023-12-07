# 方法1
def Singleton(cls):
    instance = {}

    def singleton(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return singleton


@Singleton
class MyClass:
    def __init__(self, a):
        self.a = a


a = MyClass(10)
b = MyClass(20)
print(id(a))
print(id(b))
