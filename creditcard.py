from datetime import *
def validateCard(expiry):
    if expiry>datetime.today().date():
        print("Vaid")
    else:
        print("Expired")

validateCard(date(2023,11,12))
validateCard(date(2023,4,15))
