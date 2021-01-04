hrs = input("Enter Hours:")
h = float(hrs) #convert hours to float#
rate = input("Enter Hourly Pay Rate:")
r = float(rate) #convert pay rate to float#

if h <= 40 : #overtime or not?#
    pay = (h * r) #calculate regular pay#
else:
    ot = h - 40 #calculate overtime hours#
    bigpay = ((h - ot) * r) + (ot * 1.5 *r) #calculate overtime pay#
    print(bigpay)
