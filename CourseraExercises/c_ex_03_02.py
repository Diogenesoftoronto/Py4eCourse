
hrs = input("Enter Hours: ")
rate = input('Enter your wage rate: ')
hrs = float(hrs)
rate = float(rate)
ohrs = hrs-40.0
orate = rate*1.5
opay = ohrs*orate
if hrs >= 40:
    hrs = hrs-ohrs
    pay = hrs * rate
    x = pay+opay
    print("Pay :",x)
else:
    print ("Pay:",pay)