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
            print(f"֧支付宝支付{money}花呗支付")


class Wechat(Payment):
    def pay(self, money):
        print(f"微信支付{money}花呗支付")


class PaymentFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_payment(self):
        pass


class AlipayFactory(PaymentFactory):
    def create_payment(self):
        return Alipay()


class WechatFactory(PaymentFactory):
    def create_payment(self):
        return Wechat()


class HuabeiFactory(PaymentFactory):
    def create_payment(self):
        return Alipay(huabei=True)


pf = HuabeiFactory()
p = pf.create_payment()
p.pay(100)

"""
关键点来了，如果我们想要增加一个类和方法那么只需要新增一个类和工厂即可
优点:
每个具体产品都对应一个具体工厂类，不需要修改工厂代码
隐藏了对象创建的实现细节
缺点：
每增加一个具体产品类，就必须增加一个相应的具体工厂类
"""


class BankPay(Payment):
    def pay(self, money):
        print(f"银行支付{money}花呗支付")


class BankFactory(PaymentFactory):
    def create_payment(self):
        return BankPay()


bank = BankFactory()
bank_pay = bank.create_payment()
bank_pay.pay(100)
