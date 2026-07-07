# count = 0
# def counter():
#     def inner():
#         global count
#         count += 1
#         return count
#     return inner
# count1  = counter()
# print(count1())
# print(count1())

def counter():
    count = 0
    def inner():
        # 引用外层变量的关键字
        nonlocal count 
        count += 1
        return count
    return inner
count1 = counter()
print(count1())
