from abc import ABCMeta, abstractmethod

"""
内容:定义一系列的算法, 把它们一个个封装起来,并且使得它们可以相互替换,本模式使得算法
可以独立与使用它的客户而变化.
角色
抽象策略 strategy
具体策略 concretestrategy
上下文 context

假设两种算法,一种算法准确度高,但是计算时间长
一种算法,很快 但是只能近似选一种比较好的方案
如何在两种算法之间切换就是策略模式
"""


class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, data):
        pass


class FasterStrategy(Strategy):
    def execute(self, data):
        print(f"用较快的策略处理{data}")


class SlowStrategy(Strategy):
    def execute(self, data):
        print(f"用较慢的策略处理{data}")


class Context:
    def __init__(self, strategy, data):
        self.strategy = strategy
        self.data = data

    def set_strategy(self, strategy):
        self.strategy = strategy

    def do_strategy(self):
        self.strategy.execute(self.data)


data = '[...]'
s1 = FasterStrategy()
s2 = SlowStrategy()
context = Context(s1, data)
context.do_strategy()
context.set_strategy(s2)
context.do_strategy()
