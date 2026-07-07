num = 10
if num > 0 :
    print("True")
elif num == 0:
    print("Zero")
else:
    print("False")

match num:
    case 0:
        print("Zero")
    case 1:
        print("One")
    case _:
        print("Other")
# while num > 0:
#     print(num)
#     num -= 1

# for i in range(10):
#     print(i)

for i in range(1, 10, 2):
    print(i)

for i in range(10, 0, -1):
    print(i)
