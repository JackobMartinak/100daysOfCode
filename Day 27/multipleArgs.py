class Car:
    def __init__(self, **kw):
        # using get and if not found returns NONE
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="Skyline")
print(my_car.model)


def add(*args):  # *args unlimited positional arguments
    n = 0
    for i in args:
        n += i
    return n


f = add(15, 15, 2, 14, 124, 541, 21, 41)


def calculate(n, **kwargs):
    print(kwargs)
    # for key, val in kwargs.items():
    #     print(key)
    #     print(val)
    # print(kwargs["add"])
    n += kwargs.get("add")
    n *= kwargs.get("multiply")
    print(n)


calculate(2, add=3, multiply=5)
