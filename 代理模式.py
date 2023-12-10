"""
代理模式:
为其他对象提供一种代理以控制这个对象的访问
应用场景:
远程代理:为远程代理对象提供代理
虚拟代理: 根据需要创建很大的对象
保护代理: 控制对原始对象的访问,用于对象有不同访问权限
"""
from abc import ABCMeta, abstractmethod


class Subject(metaclass=ABCMeta):
    @abstractmethod
    def get_content(self):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


# 创建一个真是对象
class RealSubject(Subject):
    def __init__(self, filename):
        self.filename = filename
        f = open(filename, 'r')
        self.content = f.read()
        f.close()

    def get_content(self):
        return self.content

    def set_content(self):
        f = open(self.filename, 'w')
        f.write(self.content)
        f.close()


"""
如果我们直接调用函数的话,那么在一开始就需要创建对象
subject = RealSubject('text.txt')
此时声明对象的瞬间,就会执行init内的读取操作
如果这时候text文件非常大的话,就会占用比较大的内存
这时候可以采用虚拟代理来进行优化
"""


# 虚拟代理
class VirtualSubject(Subject):
    def __init__(self, filename):
        self.filename = filename
        self.subject = None

    def get_content(self):
        if not self.subject:
            self.subject = RealSubject(self.filename)
        return self.subject.get_content()

    def set_content(self, content):
        if not self.subject:
            self.subject = RealSubject(self.filename)
        return self.set_content(content)


class ProtectedSubject(Subject):
    def __init__(self, filename):
        self.subject = RealSubject(filename)

    def get_content(self):
        return self.subject.get_content()

    # 保护代理将拒绝写入权限
    def set_content(self, content):
        raise PermissionError('无写入权限')
