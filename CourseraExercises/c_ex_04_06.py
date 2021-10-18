def computepay(h, r):
    h = float(h)
    r = float(r)
    ohrs = h - 40.0
    orate = r * 1.5
    opay = ohrs * orate
    if hrs >= 40:
        h = h - ohrs
        pay = h * r
        tpay = pay + opay
        return tpay
    else:
        pay = h * r
        print("Pay:", pay)
    return pay

hrs = input("Enter Hours: ")
rate = input('Enter your wage rate: ')
hrs = float(hrs)
rate = float(rate)
p = computepay(hrs, rate)
print("Pay", p)