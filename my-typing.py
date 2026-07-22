from typing import Union

x: list[int] = [1, "2"]

print(x, "x")

y: str = "john"
# print(y.title())

z: bytes = b"123"  # 只支持ASCII
# print(z[1])
h: float = 0.1 + 0.2

# print(h, "h")

g: bool = True

f: float | bool = 3.14  # Union type: float or bool

j: Union[int, str, dict] = "hello"


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


def myfunc(p: Person):
    print(p.name, p.age)


myfunc(Person("John", 30))
