lst = [10,20,30,"shivu",20.98]
print(lst)
print(lst[3])
print(lst[3:5])
print(lst[::-1])
print(lst*5)
print(len(lst))

lst.append(40)
lst.remove('shivu')
del(lst[1])
print(lst)

# lst.clear()
# print(lst)

lst.insert(2,99)
print(lst)

print(max(lst))
print(min(lst))

lst.sort(reverse=True)
print(lst)
