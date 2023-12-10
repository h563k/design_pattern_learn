from abc import ABCMeta, abstractmethod


class Handler(metaclass=ABCMeta):
    @abstractmethod
    # 请假系统
    def handle_leave(self, day):
        pass


class GeneraManager(Handler):
    def handle_leave(self, day):
        if day <= 10:
            print(f"总经理批准{day}天")
        else:
            print("滚犊子")


class DepartamentoManager(Handler):
    def __init__(self):
        self.next = GeneraManager()

    def handle_leave(self, day):
        if day <= 5:
            print(f"部门经理准假{day}天")
        else:
            print(f"部门经理权力不足")
            self.next.handle_leave(day)


class ProjectManager(Handler):
    def __init__(self):
        self.next = DepartamentoManager()

    def handle_leave(self, day):
        if day <= 3:
            print(f"项目主管准假{day}天")
        else:
            print(f"项目主管权力不足")
            self.next.handle_leave(day)


day = 4
handler = ProjectManager()
handler.handle_leave(day)
"""
适用场景:
有多个对象可以处理一个请求,哪个对象处理由运行时决定
在不明确接收者的情况下. 向多个对象中的一个提交请求
优点:
降低耦合度: 一个对象无需知道是其他哪一个对象处理请求
"""