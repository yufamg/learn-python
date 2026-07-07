def add(a, b):
    return a + b


print(add(1, 2))


def min_max(nums):
    return min(nums), max(nums)


def request(url, /, d, *, data, **kvargs):
    info = {
        "url": url,
        "data": data,
        **kvargs,
    }
    print(info, d)


request("test/a", data={"name": 123}, header={}, d=99)
# print(min_max([3, 1, 4, 1, 5, 9, 2, 6]))
# print(sorted([3, 1, 4, 1, 5, 9, 2, 6], key=lambda x: x))
# add = lambda x, y: x + y
# print(add(1, 2))


def addNums(a, b, *nums, **options):
    print(options)
    return a + b + sum(nums)


result = addNums(1, 2, 3, 4, name="Alice", age=25)
print(result)
