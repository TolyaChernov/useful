import time


def time_decorate(func):
    def wrapper(*args, **kwargs):

        start = time.time()
        result = func(*args)
        stop = time.time()
        print(f"Total: {stop - start}")
        return result

    return wrapper

@ time_decorate
def calc(lst):
    print(sum(lst))


a = [8456498968461, 89797546792, 46857946573, 6564984, 50000, 6000]
# calc = time_decorate(calc)
calc(a)
