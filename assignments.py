# firstName = "Shivranjan"
# print("First name of the candidate is" ,firstName)
# lastName = "Joshi"
# print("Surname fo the candidate is" ,lastName)
# age = "18"
# print("Age of the candidate is" ,int(age))
# DOB = "21 nov 2003"
# print("Date of birth of candidate is" ,str(DOB))
# ssn = "9876"
# print("Social security number:" ,int(ssn))
# height = "181.2"
# print("Height:" ,float(height))
# weight = "72.5"
# print("Weight:" ,float(weight))


# lst = ['India','USA','Russia']
# print(lst)
# lst.append('Australia')
# print(lst)
# lst.remove(lst[2])
# lst.insert(2,'China')

# height = 6.2
# weight = 75
# #BMI = weight in kg/height in metres ka square
#
# heightinm = height*0.4536
#
# bmi = (weight)/(heightinm*heightinm)
# print('BMI', bmi)
#
# def calculateBMI(height,weight):
#     heightinm = height * 0.4536
#     bmi = (weight) / (heightinm * heightinm)
#     return bmi

# print(calculateBMI(5.8,76))


# a =90
# b= 89
# sum=67
# sum+=a+b
# print(sum)
# print(type(sum))

# print("Onions,lettuce,tomato,olives,pepper,tomatoes")
# lst = [x for x in input("Select any three toppings from above:").split()]
# print(lst)
# s=int(input("How many sandwiches:"))
# print("Total billing amount is:",s*5,"$")
#
# m,p,c = [float(x) for x in input("Enter marks got in maths, physics and chemistry:").split()]
# if m<35 or p<35 or c<35:
#     print("You have failed the exam")
# else:
#     average = (m+p+c)/3
#     print(average)
#     print("You have passed the exam")
#     if average<=59:
#         print("You have got C grade")
#     elif average>59 and average<=69:
#         print("You have got B grade")
#     else:
#         print("You have got A grade")
#
# x = int(input("Enter a number:"))
# for i in range(x+1):
#     if i%10 == 0:
#         continue
#     if i>100:
#         break
#     print(i)

# primeFlag = False
# x = int(input("Enter a number:"))
# for i in range(2,x):
#     if x%i == 0:
#         primeFlag = True
#
# if (primeFlag==True):
#     print(x,"is not prime")
# else:
#     print(x,"is a prime")

# import sys
# lst = sys.argv
#
# print("1: Check balance")
# print("2: WithDraw Cash")
# print("3: Deposit Cash")
# print("4: Deposit Check")
#
# accBalance = 10000
#
# option = int(input("Choose from the options provided above: "))
#
# if option == 1:
#     print("You have entered to check your balance which is:", accBalance)
# elif option == 2:
#
#     withDraw = int(input("Enter the amount to be withdrawn:"))
#     accBalance = accBalance-withDraw
#     print("New balance is: ", accBalance)
# elif option == 3:
#     Depositcash = int(input("Enter the amount to be deposited:"))
#     accBalance = accBalance + Depositcash
#     print("New balance is:", accBalance)
#
# elif option == 4:
#     Depositcheck = int(input("Enter the amount to be deposited through check:"))
#     accBalance = accBalance+Depositcheck
#     print("New balance is:", accBalance)
#
# else:
#     print("Enter a valid option!")

# n= int(input("Enter a number"))
# for i in range(0,n):
#     print(i**2)

# n = int(input())
# i=0
# while i<n:
#     i+=1
#     print(i)

n=int(input())
t=map(int, input().split())
print(list(t))