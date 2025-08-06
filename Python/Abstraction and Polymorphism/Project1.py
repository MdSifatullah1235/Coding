from abc import ABC, abstractmethod

class ABClass(ABC):
    def print(self, z):
        print("Passed Down Value", z)

    @abstractmethod

    def task(self):
        print("We are inside abstract class")

class test(ABClass):
    def task(self):
        print("We are inside test class")

t1 = test()
t1.task()
t1.print(10)