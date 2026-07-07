# for x in range(2, 10):
#     for y in range(2, x):
#         if x % y == 0:
#             print(x, "equals", y, "*", x // y)
#             break
#     else:
#         # else 在 for 循环正常结束时执行，即没有遇到 break 语句时执行
#         print(x, "is a prime number")
# # 一个循环的 else 子句会在未发生 break 时运行


# # point 是一个 (x, y) 元组
# point = (1, 2)
# match point:
#     case (0, 0):
#         print("Origin")
#     case (0, y):
#         print(f"Y={y}")
#     case (x, 0):
#         print(f"X={x}")
#     case (x, y) if x == y:
#         print(f"X={x}, Y={y}")
#     case _:
#         raise ValueError("Not a point")

from enum import Enum


class Color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"


color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))

match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print("I'm feeling the blues :(")
