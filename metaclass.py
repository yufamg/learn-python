class Foo:
    pass


f = Foo()
print(type(f).__name__)

# 动态创建类

Hello = type("Hello", (object,), {"hello": lambda self, y: print(y)})


hello = Hello()
print(Hello)
print(type(Hello))
hello.hello("123")
