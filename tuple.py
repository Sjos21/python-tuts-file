tpl = (20,30,20,'shivu')
# tpl[2] = 123----->tuple is immutable
print(tpl*3)
print(tpl.count(20))
print(tpl.index('shivu'))
print(tpl[:2])

lst = [67,43,"xyz"]
print(type(lst))
tpl1 = tuple(lst)
print(type(tpl1))
print(tpl1)