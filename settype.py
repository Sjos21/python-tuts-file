s={10,20,30,"xyz",10,20}

s.update({88,99})
print(type(s))

s.remove(30)
print(s)

f = frozenset(s)
# f.remove({20})


r = {10,20,90,80}
r.update((56,67))
print(r)