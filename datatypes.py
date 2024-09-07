#UseCase
id=1
FirstName="John"
LastName="   Belly"
ssn='123-456-789-0'
hasInsurance=True
BillingAmount="1000"
BillingAmount=float(BillingAmount)
print(type(BillingAmount))

print(id, FirstName, LastName.lstrip(), ssn, hasInsurance, BillingAmount, ssn[8:len(ssn)])
