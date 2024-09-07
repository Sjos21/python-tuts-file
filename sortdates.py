from datetime import date
import time
starttime=time.perf_counter()
ldates=[]
d1=date(2056,9,27)
d2=date(2009,9,27)
d3=date(2023,9,27)

ldates.append(d1)
ldates.append(d2)
ldates.append(d3)
ldates.sort()

time.sleep(3)
for d in ldates:
    print(d)

endtime=time.perf_counter() #perf_counter gives the time in which the code gets executed till it's end.(having starttime and endtime as the parameter
#here)
print("execution time", endtime-starttime)