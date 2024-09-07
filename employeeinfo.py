n = int(input("Enter the no. of employee"))
employees = {}
for i in range(n):
    name = input('Enter employee name')
    salary = input('Enter employee salary')
    employees[name] = salary
print("You can know the salary detail by going through employees individually")
while True:
    name = input('Enter employee name')
    salary = employees.get(name, -1)
    if salary == -1:
        print("Employee does not exist")
    else:
        print("Salary of employee is", salary)
    choice = input("Do you want o know about other employees[Yes|No]")
    if choice == 'No':
        break
