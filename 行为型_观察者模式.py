from abc import ABCMeta, abstractmethod

"""
内容:定义对象的一种一对多分依赖关系,当一个对象的状态发生改变时候,所有依赖于它的
对象都得到通知并被自动更新.观察者模式又称为{发布-订阅}模式
角色
抽象主题 subject
具体主题 concretesubject --发布者
抽象观察者 observe
具体观察者 concreteobserve --订阅者

我们希望发布订阅能做到以下特性
1. 观察对象一旦发生更新后,希望能够立即通知所有订阅者,而不需要自己去查询跟新
2. 订阅应当是松耦合,随时可以取消和重新订阅
"""


class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, notice):  # 处理notice类
        pass


class Notice:  # 发布者
    # 比较好的办法就是利用一个列表来维护订阅机制
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self)


class StaffNotice(Notice):  # 具体发布者
    def __init__(self, company_info=None):
        # 调用父类关系
        super().__init__()
        # 这里用私有类去定义
        self.__company_info = company_info

    @property
    # property使得可以访问__company_info的信息
    def company_info(self):
        return self.__company_info

    """
    setter使得__company_info内容可以修改
    一旦__company_info发生修改,那么就可以触发notify去通知
    """

    @company_info.setter
    def company_info(self, info):
        self.__company_info = info
        self.notify()


class Staff(Observer):
    def __init__(self):
        self.company_info = None

    def update(self, notice):
        self.company_info = notice.company_info


notice = StaffNotice("初始发布信息")
s1 = Staff()
s2 = Staff()
notice.attach(s1)
notice.attach(s2)
print(s1.company_info, s2.company_info)
notice.company_info = "公司今年业绩不错,给大家发奖金\n"
print(s1.company_info, s2.company_info)
notice.detach(s2)
notice.company_info = "公司明天放假\n"
print(s1.company_info, s2.company_info)
