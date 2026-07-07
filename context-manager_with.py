# 上下文管理器（with）
from contextlib import contextmanager,suppress,closing
import os
# 
f = open('mock.json')
data = f.read()
f.close()
print(data)

with open('mock.json') as f:
    data = f.read()
    print(data)

class MyContextManager:
    def __init__(self,name):
        self.name = name
    def __enter__(self):
        print(f'{self.name} enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'{self.name} exit')
        return True # 忽略捕获异常

with MyContextManager(name='John') as cm:
    print('hello', cm)
    raise ValueError('value sssss error')

@contextmanager
def my_context_manager():
    try:
        print('enter')
        yield [1,2,3]
        # raise ValueError('value error')
    except ValueError as e:
        print('error', e)
    else:
        print('no error')
    finally:
         print('exit')
with my_context_manager() as cm:
    print('hello', cm)

with suppress(FileNotFoundError): # 抑制特定异常 忽略异常
    os.remove('test.txt')

# 自动实现协议 要有close方法
class MyContextManagerAuto:
    def __init__(self,name):
        self.name = name
    def close(self):
        print(f'{self.name} close')
    # def __enter__(self):
    #     print(f'{self.name} enter')
    #     return self

    # def __exit__(self, exc_type, exc_val, exc_tb):
    #     print(f'{self.name} exit')
    #     return True # 忽略捕获异常
with closing(MyContextManagerAuto('John')):
    print('hello')

# with适用于 有借有还、成对操作
