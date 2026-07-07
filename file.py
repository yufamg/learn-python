import json

with open("./mock.json") as f:
    # for i, line in enumerate(f):
    #     print(line, i)
    print(json.loads(f.read()))
