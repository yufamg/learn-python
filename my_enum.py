from enum import Enum, auto, unique


@unique
class Month(Enum):
    JAN = auto()
    FEB = auto()
    Mar = auto()


# 不推荐
M = Enum("M", ["JAN", "FEB"])

# print(Month.JAN)
# print(M.FEB)

for m in Month:
    print(m.name, m.value)
