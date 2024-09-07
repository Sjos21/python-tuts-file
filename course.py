class Course:
    def __init__(self,name,ratings):
        self.name = name
        self.ratings=ratings

    def average(self):
        nor = len(self.ratings)
        average = sum(self.ratings)/nor
        print("Average rating for the course ",self.name," is ",average)

c1=Course("Java", [1,2,3,4,5])
print(c1.name)
print(c1.ratings)
c1.average()

c2 = Course("Python", [1,2,3,4,5,6,7])
print(c2.name)
print(c2.ratings)
c2.average()