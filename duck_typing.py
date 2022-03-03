from abc import ABCMeta,abstractmethod #(抽象方法)

class Payment(metaclass=ABCMeta):   # metaclass 元类  metaclass = ABCMeta表示Payment类是一个规范类
    def __init__(self,name,money):
        self.money=money
        self.name=name

    @abstractmethod      # @abstractmethod表示下面一行中的pay方法是一个必须在子类中实现的方法
    def pay(self,*args,**kwargs):
        pass

class AliPay(Payment):

    def pay(self):
        # 支付宝提供了一个网络上的联系渠道
        print('%s通过支付宝消费了%s元'%(self.name,self.money))

class WeChatPay(Payment):

    def pay(self):
        # 微信提供了一个网络上的联系渠道
        print('%s通过微信消费了%s元'%(self.name,self.money))


class Order(object):

    def account(self,pay_obj):
        pay_obj.pay()

pay_obj = WeChatPay("wang",100)
pay_obj2 = AliPay("zhang",200)

order = Order()
order.account(pay_obj)
order.account(pay_obj2)