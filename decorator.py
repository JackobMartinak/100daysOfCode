import time


def delay_decorator(fun):
    def inner_fun():
        time.sleep(2)
        fun()

    return inner_fun


@delay_decorator
def hello():
    print("Hello!")


hello()
