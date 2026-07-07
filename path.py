import json
from pathlib import Path

p = Path("./mock.json")
data = json.loads(p.read_text())
print(data)
print(type(data))
print(Path.cwd())
print(p.name)
print(p.suffix)
print(p.suffixes)
print(p.stem)
print(p.parent)
print(list(map(lambda x: x.name, p.parents)))
print(p.parts)

p1 = Path("/usr")
p2 = p1 / "bin"
print(p2)
p3 = Path("/Users/bji118-m0j6whn/Desktop/python/mock.json")
for p in p3.parents:
    print(p)
