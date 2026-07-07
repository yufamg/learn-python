# generator = (x**2 for x in range(1, 11) if x % 2 == 0)
# print(generator)
# for i in generator:
#     print(i)


def generator_function():
    for x in range(1, 11):
        if x % 2 == 0:
            yield x**2, x


generator = generator_function()
print(next(generator))
print(next(generator))
# for i, j in generator_function():
#     print(i, j)

names = ["liangdianshui", "twowater", "两点水"]
ages = [18, 19, 20, 21]
colors = ["red", "green", "blue"]
zip_object = zip(names, ages, colors)
for x in zip_object:
    print(x)
print(zip_object)

enumerate_object = enumerate(names)
for x in enumerate_object:
    print(x)
