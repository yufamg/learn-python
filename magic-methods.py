class Book:
    def __init__(self, name, list) -> None:
        self.name = name
        self.list = list

    # 未定义会回退到__repr__
    def __str__(self):
        return self.name

    # 命令行工具打印 优先
    def __repr__(self):
        return f"{self.name}"

    def __eq__(self, other: object) -> bool:
        print(f"{self=},{other=}")
        return self.name == other.name

    def __len__(self):
        return len(self.list)

    def __getitem__(self, key):
        return self.list[key]

    def __setitem__(self, key, val):
        self.list[key] = val

    def __delitem__(self, key):
        del self.list[key]


# print(Book("222", []) == Book("222", []))
# print(len(Book("11", [1, 2, 3, 4])))
# print(Book("hah", [1, 2, 3])[1])

itt = Book("hah", [1, 2, 3])
itt[0] = 99
del itt[1]
for x in itt:
    print(x)
# print(itt[0])
