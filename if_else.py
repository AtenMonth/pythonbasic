amount=int(input("enter the salary "))
totalsal=amount*12
tax=0
if totalsal<250000:
    print("no Tax")
elif totalsal<500000:
    tax=0.05*totalsal
    print("tax to be paid:Rs.",tax)
elif totalsal<1000000:
    tax=0.2*totalsal
    print("tax to be paid:Rs.",tax)
else:
    tax=0.3*totalsal
    print("tax to be paid:Rs.",tax)
