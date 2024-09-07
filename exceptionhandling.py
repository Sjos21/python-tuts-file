import logging

logging.basicConfig(filename="mylog.log",level=logging.DEBUG)

try:
    f=open("myfile", "w")
    a,b=[int(x) for x in input("Enter two numbers: ").split()]
    logging.info("Division in process")
    c=a/b
    f.write("Writing %d into file" %c)
except ZeroDivisionError:
    print("Division by zero is not allowed")
    print("Enter a different number")
    logging.error("Division by zero")
else:
    print("You have entered a non zero number")
finally:
    f.close()
    print("File is closed")
print("Code after the execution")