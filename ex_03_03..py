score = input("Enter Score: ")

try:
    ts = float(score)
except:
    print("Error, please enter numeric input")
    quit()

if ts >= 0.9:
    print("A")
elif ts >= 0.8:
    print("B")
elif ts >= 0.7:
    print("C")
elif ts >= 0.6:
    print("D")
elif ts < 0.6:
    print("F")
elif ts > 1.0:
    print("error, out of range")
else:
    print("error")