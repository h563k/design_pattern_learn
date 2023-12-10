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


"""
还是之前的支付系统，但是现在有另一套代码，也是支付系统，现在公司
想进行业务合并，把两个功能整合到一起
"""


class BankPay:
    def cost(self, money):
        print(f"银联支付{money}")


"""
之前的系统调用逻辑是这样的
p = Alipay()
p.pay(100)
但是新的代码，支付函数名字叫cost，考虑到实际中cost函数可能被另一套系统用在很多
地方，我们不希望通过重命名之类的方式对cost函数进行重构，该如何设计呢
"""


class NewBankPay(Payment, BankPay):
    def pay(self, money):
        self.cost(money)


"""
这两通过NewBankPay适配器，调用了BankPay的cost函数
但是表现形式采用了Payment的形式
这么写实现了初步的适配器模式，但是 如果还有更多的银行支付系统需要接入呢？
那么就需要把这个适配器进行抽象化
"""
p = NewBankPay()
p.pay(100)


class ApplePay:
    def cost(self, money):
        print(f"苹果支付{money}")


class PaymentAdapter(Payment):
    def __init__(self, payment):
        self.payment = payment

    def pay(self, money):
        self.payment.cost(money)


"""
将一个类的接口转行成客户端希望的另一个接口.
适配器模式使得原本由于接口不兼容而不能一起工作的类可以一起工作
两种实现方式
类适配器: 采用多继承方式
对象适配器: 使用组合
"""
p = PaymentAdapter(NewBankPay())
p.pay(100)
p = PaymentAdapter(ApplePay())
p.pay(100)
