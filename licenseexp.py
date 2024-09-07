class tooYoungException(Exception):
    def __init__(self, msg):
        self.msg=msg

class tooOldException(Exception):
    def __int__(self, msg):
        self.msg=msg

age=int(input("Enter an age: "))
if age<18:
    raise tooYoungException("You have to be oder than 18 to get a license")
elif age>90:
    raise tooOldException("You are too old to drive any vehicle")
else:
    print("You are eligible")
