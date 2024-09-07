class Product:
    def __init__(self):                         #<----constructor
        self.name= 'Iphone'
        self.description = 'Its Awesome'
        self.price = 700

    def __del__(self):
        print("Inside the destuctor")

    def display(self):                          #<----instance method
        print(self.name)
        print(self.price)
        print(self.description)

p1 = Product()
p1.display()
p1 = None

