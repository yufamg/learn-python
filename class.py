from dataclasses import dataclass


class Dog:
    name = "Dog"
    """ Dog name """

    tricks = []

    def __init__(self, name):
        self.name = name
        self.tricks = []  # 为每个 Dog 实例新建一个空列表

    def add_trick(self, trick):
        self.tricks.append(trick)

    __age = 0


d = Dog("Buddy")
print(d.__age)


@dataclass
class DataA:
    name: str
    """ DataA name """


print(DataA(name="Alice"))
