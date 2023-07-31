hrs = input("Enter Hourts: ")
rate = input("Enter Rate: ")

try:
    h = float(hrs)
    r = float(rate)
except:
    print("Error, please enter numeric input")
    quit()

def computepay(h, r):
    if h > 40:
        reg = h * r
        otp = (h - 40.0) * (r * 0.5)
        p = reg + otp
    else:
        p = h * r

    return p

p = computepay(h, r)
print("Pay", p)
