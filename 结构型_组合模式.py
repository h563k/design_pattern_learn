"""
实用场景：
ppt里面我们可以把方框 圆圈通过右键进行组合
组合后的形状和单个形状一样，有复制、粘贴等功能
"""
from abc import ABCMeta, abstractmethod


# 如何实现不同的形状统一接口，我们需要一个统一的处理器
# 抽象组件
class Graphic(metaclass=ABCMeta):
    @abstractmethod
    def draw(self):
        pass


class Point(Graphic):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"点{self.x},{self.y}"

    def draw(self):
        print(str(self))


# 叶子组件
class Line(Graphic):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return f"线段{self.p1},{self.p2}"

    def draw(self):
        print(str(self))


# 复合组件
class Picture(Graphic):
    def __init__(self, iterable):
        self.children = []
        for i in iterable:
            self.add(i)

    def add(self, graphic):
        self.children.append(graphic)

    def draw(self):
        print('---------')
        for child in self.children:
            child.draw()
        print('---------')


point1 = Point(2, 3)
line1 = Line(Point(1, 1), Point(4, 5))
line2 = Line(Point(6, 6), Point(9, 9))
picture1 = Picture([point1, line1, line2])
picture1.draw()

point2 = Point(10, 11)
line3 = Line(point2, Point(13, 15))
picture2 = Picture([point2, line3])
picture2.draw()

picture = Picture([picture1, picture2])
picture.draw()

"""
组合模式具有一定的使用场景限制
1、对象需要满足部分-整体的层次结构（最好是可递归的）
2、希望用户忽略组合对象与单个对象的不同。
3、组合相对自由，能够根据客户需要去生成多种组合对象
（你可以把单个元素组合成组件，然后把组件组合）
"""
