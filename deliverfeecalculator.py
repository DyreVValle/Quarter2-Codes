def deliveryfee(distancekm, rate):
    return print("Delivery fee is: ₱", {distancekm * rate})

distancekm = float(input("Enter distance in kilometers: "))
rate = float(input("Enter rate per kilometer: "))

deliveryfee(distancekm, rate)