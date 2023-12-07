"""
假设一种场景,我要创建一种类,这个类有一个维度长度
那么 我们可以创建不同的类,short类 long类等等
但是接下来我们增加了一个维度:颜色,这种时候,我们应该怎么办?
比较好理解的方式就是,如果要创建个红色短的类,继承short类后创建一个red_short类
但是随着颜色不断增加,创建类的数量可能会变成两个维度的数量乘积,大大增加工作量
桥接的目的就是对不同维度进行解耦
"""
from abc import ABCMeta, abstractmethod


class Shape(metaclass=ABCMeta):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def draw(self):
        pass


class Color(metaclass=ABCMeta):
    @abstractmethod
    def paint(self, shape):
        pass


class Rectangle(Shape):
    name = "长方形"

    def draw(self):
        self.color.paint(self)


class Circle(Shape):
    name = "圆形"

    def draw(self):
        self.color.paint(self)


class Red(Color):
    def paint(self, shape):
        print(f"红色的{shape.name}")


class Yellow(Color):
    def paint(self, shape):
        print(f"黄色的{shape.name}")


# 接下来创建
shape = Rectangle(Red())
shape.draw()
shape = Circle(Red())
shape.draw()
shape = Rectangle(Yellow())
shape.draw()

# 长度和颜色 可以在维度上进一步扩展
