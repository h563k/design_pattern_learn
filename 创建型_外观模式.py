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
