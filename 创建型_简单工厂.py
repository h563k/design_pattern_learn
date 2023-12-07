from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass


class Alipay(Payment):
    def __init__(self, huabei=False):
        self.huabei = huabei

    def pay(self, money):
        if self.huabei:
            print(f"花呗支付{money}元")
        else:
            print(f"支付宝支付{money}元")


class Wechat(Payment):
    def pay(self, money):
        print(f"微信支付{money}元")


class PaymentFactory:
    def create_payment(self, method):
        if method == 'alipay':
            return Alipay()
        elif method == 'wechat':
            return Wechat()
        elif method == 'huabei':
            return Alipay(huabei=True)
        else:
            print("无此方法")

"""
能过隐藏具体实现方式
违反开闭原则
"""
pf = PaymentFactory()
p = pf.create_payment('huabei')
p.pay(100)
