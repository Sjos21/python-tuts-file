# n=int(input())
# for i in range(n):
#     a,b=map(int,input().split())
#     ans1=0
#     ans2=0
#     counta=0
#     countb=0
#     while a>0:
#         rem=a%10
#         ans1+=rem
#         a=a//10
#
#     while b>0:
#         rem1=b%10
#         ans2+=rem1
#         b=b//10
#     if ans1>ans2:
#         counta+=1
#     elif ans1<ans2:
#         countb+=1
#     else:
#         counta+=1
#         countb+=1
#
# if counta>countb:
#     print(0,counta)
# elif counta<countb:
#     print(1,countb)
# elif counta==countb:
#     print(2,counta)
import math
# from collections import
# l=[2,3,3,4]
# k=min(l)
# l.remove(k)
# j=min(l)
# print(
# print((13//7)+1)

# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n*factorial(n-1)
# m=[2.'apple',3.5]
# print(15//8)

# class InvalidPasswordException(Exception):
#     def __init__(self, msg):
#         self.msg=msg
#
# try:
#     password=input("Enter your password: ")
#     if len(password)<8:
#         raise InvalidPasswordException("Password's length should not be less than 8")
# except InvalidPasswordException as obj:
#     print(obj)
# else:
#     print("Password is saved respectively")

# from threading import *
# def evenNumbersThread():
#     for i in range(2,101,2):
#         print(i)
# def oddNumbersThread():
#     for i in range(1,101,2):
#         print(i)
# def mainThread():
#     for i in range(1,101):
#         print(i)
#
# t1=Thread(target=evenNumbersThread)
# t2=Thread(target=oddNumbersThread)
# t1.start()
# t2.start()
#

# mainThread()

# from threading import *
#
# class evenNumbersThread:
#     def __init__(self):
#         self.c = Condition()
#     def display(self):
#         self.c.acquire()
#         for i in range(2,101,2):
#             print(i,end=" ")
#         print()
#         self.c.notify()
#         self.c.release()
#
# class oddNumbersThread:
#     def __init__(self,even):
#         self.even=even
#     def display(self):
#         self.even.c.acquire()
#         for i in range(1,101,2):
#             print(i,end=" ")
#         print()
#         self.even.c.notify()
#         self.even.c.release()
#
# even=evenNumbersThread()
# odd=oddNumbersThread(even)
# t1=Thread(target=even.display)
# t2=Thread(target=odd.display)
# t1.start()
# t2.start()
#
# def main_Thread():
#     even.c.acquire()
#     for i in range(1,101):
#         print(i,end=" ")
#     even.c.notify()
#     even.c.release()
#
# t3=Thread(target=main_Thread)
# t3.start()

# print(len(str(7*5)))
# side=int(input())
# print("Enter a number :",side)
# print("The star pattern for the given number is:\n")
# a=list(map(int,input().split()))
# zeros=a.count('0')
# print(zeros)
# print(len(a))
# l=len(a)//2
# print(l)
# if a.count("0")>=l:
#     print("No")
# else:
#     print("Yes")
# import numpy as np
# a=list(map(int,input().split()))
# b=list(map(int,input().split()))
# l1=[]
# l2=[]
# l3=[]
# for i in a and b:
#     l1.append(i*20)
#     l2.append(i*10)
# l3.append(np.subtract(l1,l2))
# print(*l3)
# print(max(*l3

# n=int(input())
# temp=n
# rem=0
# while(temp>0):
#     ans=temp%10
#     rem=(rem*10)+ans
#     temp=temp//10
# if rem==n:
#     print("A palindrome")
# else:
#     print("Not a Palindrome")

# s=str(input())
# if s==s[::-1]:
#     print("A palindromic string")
# else:
#     print("Not a palindromic string")

# def amstr(n):
#     sum=0
#     temp=n
#     while(temp>0):
#         ans=temp%10
#         sum+=ans**3
#         temp//=10
#     if sum==n:
#         return "Number is Armstrong"
#     else:
#         return "Number is not Armstrong"
# print(amstr(153))
# def fib(n):
#     if n==0:
#         return 1
#     if n==1:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
#
# n=int(input("Enter a number"))
# print(fib(n))
# def isAnagram(s1,s2):
#     if sorted(s1)!=sorted(s2):
#         return False
#     return True
#
#
# s1=input()
# s2=input()
# if isAnagram(s1,s2):
#     print("YES")
# else:
#     print("NO")

# l=[1,2,1,3,3,0,4,4]
# print(set(l))
# def add(n1,n2):
#     return n1+n2
#
# def subtract(n1,n2):
#     return n1-n2
#
# def multiply(n1,n2):
#     return n1*n2
#
# def division(n1,n2):
#     return n1//n2
#
# print("Select Operation: ")
# print("1.Add")
# print("2.Subtract")
# print("3.Multiply")
# print("4.Division")
#
# while True:
#     choice=input("Enter choice from 1/2/3/4: ")
#     if choice in ('1', '2', '3', '4'):
#         n1 = int(input("Enter first number: "))
#         n2 = int(input("Enter second number: "))
#     if choice=='1':
#         print(n1, "+", n2, "=", add(n1,n2))
#     elif choice=='2':
#         print(n1, "-", n2, "=", subtract(n1,n2))
#     elif choice=='3':
#         print(n1, "*", n2, "=", multiply(n1,n2))
#     elif choice=='4':
#         print(n1, "/", n2, "=", division(n1,n2))
#     else:
#         print("Enter a valid choice number")
#
#     next=input("Do you want to do another calculation? Y/N: ")
#     if next=='N':
#         print("Teri maa ki burr")
#         break


# n=6
# m=2
# mini=min(n,m)
# ans=(n+m)//4
# if ans<=mini:
#     print(ans)
# else:
#     print(mini)

# n=int(input())
# arr=list(map(int,input().split()))
# s=set(arr)
# sorted(s)
# s1=list(s)
# if len(s)==1:
#     print(s.pop())
# else:
#     print(s1[1])

# to print out an element from set we use pop() function since set in python contain elements in an unordered way i.e. without indexing
# to convert into list from set use list() function and vice versa if to convert into set from list i.e. using set() function


from collections import Counter
# n=int(input())
# l=[]
# for i in range(n):
#     s=input()
#     l.append(s)
#
# counter=Counter(l)
# ans=max(counter, key=counter.get)
# print(ans)

n=int(input())
# l=[]
# for i in range(n):
#     s=input()
#     l.append(s)
#
# counter=Counter(l)
# print(max(counter,key=counter.get),max(counter.values()))

# a=list(map(int,input().split()))
# mini,maxi=min(a),max(a)
# l=[]
# for i in range(len(a)):
#     if a[i]==maxi:
#         l.append(a[i])
#     if a[i]==mini:
#         l.append(a[i])
# s=set(l)
# again=reversed(list(s))
# print(*again)
arr=list(map(int,input().split()))
mini=arr[0]
maxi=arr[0]
for i in range(n):
    if (arr[i]<mini):
        mini=arr[i]
    if (arr[i]>maxi):
        maxi=arr[i]

print(maxi,mini)    #this code eliminates our need to convert list into set and then into list once again to have less time complexity and our code is more optimal. Can address the issue of having duplicates in our array.




