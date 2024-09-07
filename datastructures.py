students={'John':['Python', 'DJango', 'C++'], 'Bob':['Java','JS'], 'Jim':['Ruby','Node.Js']}
keys = students.keys()
for eachKey in keys:
    print('Courses taken by', eachKey,'are: ')
    for eachCourse in students[eachKey]:
        print(eachCourse)