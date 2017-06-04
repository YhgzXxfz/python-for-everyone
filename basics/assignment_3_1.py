hrs = raw_input("Enter Hours:")
h = float(hrs)
rate = raw_input("Enter rate:")
r = float(rate)

if h <= 40 :
    pay = h*r
else :
    pay = 40*r + (h-40)*1.5*r

    
print pay
