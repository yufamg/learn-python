# import json
import random
from math import sqrt as sqrt_func

# import module.moduleA as add_func
from module.moduleA import *

# print(pi, sin(pi / 2))
print(sqrt_func(16))


def main():
    print("This is the main module")


print(__name__)
# if __name__ == "__main__":
#     main()
print(add(1, 2))
print(subtract(5, 3))
print(random.choices([1, 2, 3], k=2))
# print(random.randint(1, 1000))
# dics = {"name": 123}
# print(json.loads(json.dumps(dics)))
