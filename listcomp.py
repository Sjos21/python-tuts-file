#cubes of number:
#regular programming:
# lst=[]
# for x in range(1,11):
#     lst.append(x**3)
# print(lst)

#list compre.:

# lst = []
# lst = [x**3 for x in range(1,11)]
# print(lst)

#even nos. using list comp.:

# lst=[x for x in range(2,21,2)]
# print(lst)
#
# lst=[x for x in range(1,21) if x%2==0]
# print(lst)

#product of elements using list comp.:
#regular coding:
# a = [1,2,3,4,5]
# b = [6,7,8,9,10]
# s= []
#  for i in range(len(a)):
#      s.append(a[i]*b[i])
#list compre.:
# s=[a[i]*b[i] for i in range(len(a))]
# print(s)

#common elements in a list:
#regular coding:
a=[2,4,6,8]
b=[1,2,3,4]
result = []
# for i in a:
#     if i in b:
#         result.append(i)
#list compre.:
result=[i for i in a if i in b]
print(result)

