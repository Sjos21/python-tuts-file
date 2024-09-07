from datetime import *
d=date(2023,8,12)
t=time(11,39)
dt=datetime.combine(d,t)
print(dt)

td=datetime.today()
print(td)
# now and today give the same output when used simultaneously in a program
td=datetime.now()
print(td)