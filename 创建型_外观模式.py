from abc import ABCMeta, abstractmethod


class CPU:
    def run(self):
        print("cpu开始工作")

    def stop(self):
        print("cpu停止工作")


class Disk:
    def run(self):
        print("硬盘开始工作")

    def stop(self):
        print("硬盘停止工作")


class Memory:
    def run(self):
        print("内存开始工作")

    def stop(self):
        print("内存停止工作")


class Computer:  # 外观模式封装
    def __init__(self):
        self.cpu = CPU()
        self.disk = Disk()
        self.memory = Memory()

    def run(self):
        self.cpu.run()
        self.disk.run()
        self.memory.run()

    def stop(self):
        self.cpu.stop()
        self.disk.stop()
        self.memory.stop()


computer = Computer()
computer.run()
computer.stop()

"""
为子系统中的一组接口提供一个一致的界面,外观模式定义了一个高层接口
这个接口使得这一子系统更加容易使用.
角色
外观 faceade
子系统 subsystem classes
"""




