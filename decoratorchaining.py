def sqaure(fun):
    def inner():
        n = fun()
        return n*n
    return inner

def half(fun):
    def inner():
        n = fun()
        return n/2
    return inner

@sqaure
@half
def num():
    return 10

print(num())