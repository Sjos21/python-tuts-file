#right angled triangle:
# n = int(input("Enter the no. of rows:"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("* ",end="")
#     print()

# n = int(input("Enter the no. of rows:"))
# for i in range(1,n+1):
#     print("* "*i)


#pyramid pattern:
n = int(input("Enter the no. of rows:"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("* "*i)