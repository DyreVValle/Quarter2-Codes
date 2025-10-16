def fuelefficiency(kilometers,liters):
    if liters == 0:
        return 0
    return print("Fuel Efficiency: ", kilometers / liters, "km/L")

kilometers = float(input("Enter distance travelled (in kilometers): "))
liters = float(input("Enter fuel consumed (in liters): "))

fuelefficiency(kilometers, liters)