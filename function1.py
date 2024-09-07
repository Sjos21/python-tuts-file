def average(a,b):
    print(a)
    print(b)
    return (a+b)/2

print(average(b=9,a=8))

#multiple values in functions:

# def calc(a,b):
#     x=a+b
#     y=a-b
#     z=a*b
#     w=a/b
#     return x,y,z,w
# result = calc(10,8)
# print(result)
# for i in result:
#     print(i)
#

# function inside another:
# def display(name):
#     def message():
#         return "Hello "
#     result = message() + name
#     return result
#
# print(display("Shivu"))

#function as a parameter to other:
def display(fun):
    return "Hello "+fun

def name():
    return "Shivu"

print(display(name()))

