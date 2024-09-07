lst = [10,2,34,54,67,89,5]

# result = list(filter(lambda x:x%2==0, lst))
# print(result)
# for i in result:
#     print(i)


#same result but with a different code:
print(list(filter(lambda x:x%2==0,  lst)))
for i in lst:
    if i%2==0:
        print(i)