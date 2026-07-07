from dataclasses import dataclass, field

@dataclass
class Data:
    name: str
    age: int = 18
    # def __init__(self):
    #     pass

    # def __repr__(self):
    #     return "Data(name: str, age: int)"
print(Data(name="John"))

def mylist():
    return [1,2,3,4,5]

@dataclass
class Team:
    name: str
    lists: list = field(default_factory=mylist)
    sub: list = field(default_factory=list)

print(Team(name="John", lists=[1,2,3]))
print(Team(name="Divid"))

@dataclass(frozen=True)
class Player:
    name: str
    age: int
    height: float
    weight: float

p = Player(name="John", age=18, height=1.75, weight=75)
try:
    p.name = 'Divid'
    print(p)
except Exception as e:
    print("Cannot assign to field",e)

@dataclass
class Order:
    order_id: int
    customer_name: str
    order_date: str
    price: float
    count: int
    total_amount: float = field(init=False)
    def __post_init__(self):
        self.total_amount = self.count * self.price

print(Order(order_id=1, customer_name="John", order_date="2023-04-01", price=100.0, count=5))
