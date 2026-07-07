try:
    x = 1 / 0
except Exception as e:
    print("Error!", e, type(e).__name__)

def parse_age(s):
    try:
        age = int(s)
        100 / age
    except (ZeroDivisionError, ValueError):
        print('输入有问题')
    else:
        print('输入正常')
    finally:
        print('输入结束')


parse_age('25')
parse_age('0')
parse_age('abc')
class MyError(Exception):
    pass

def dowork(x:int):
    print('working')
    if x > 50:
        raise MyError('value error')
    print('working done')

try:
    dowork(60)
except MyError as e:
    print(e)
# BaseException
#  ├── SystemExit
#  ├── KeyboardInterrupt
#  ├── GeneratorExit
#  └── Exception
#       ├── ArithmeticError
#       │    ├── ZeroDivisionError
#       │    └── OverflowError
#       ├── LookupError
#       │    ├── IndexError
#       │    └── KeyError
#       ├── ValueError
#       ├── TypeError
#       ├── AttributeError
#       ├── NameError
#       ├── OSError
#       │    └── FileNotFoundError
#       └── ...