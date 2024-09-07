# l1 = eval(input("Enter a list of elements"))
# # s1 = set(l1)
# # print(s1)
# print(l1)
# l2=[]
# for each_value in l1:
#     if each_value not in l2:
#         l2.append(each_value)
# print(l2)

# count vowels 
word = input("Enter a word")
vowels = {'a', 'e', 'i', 'o', 'u'}
results = {}
for c in word:
    if c in vowels:
        results[c] = results.get(c, 0)+1
for k,v in sorted(results.items()):
    print(k, "is present", v, "times")

