class overTheLimitexception(Exception):
    def __init__(self, message):
        self.message=message





def withdraw(amount):
    if amount>500:
        raise overTheLimitexception("You cannot withdraw more than 500 dollars per day")


withdraw(600)
