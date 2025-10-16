def electricitybill(kWh):

    fixed_charge = 50

    if kWh <= 100:
        bill = kWh * 5 + fixed_charge
    elif 101 <= kWh <= 200:
        bill = kWh * 7 + fixed_charge
    elif 201 <= kWh <= 500:
        bill = kWh * 10 + fixed_charge
    else:  # kWh > 500
        bill = kWh * 12 + fixed_charge + 500

    return print("Total Electricity Bill:", bill)

kWh = float(input("Enter the number of kilowatt-hours used:"))

electricitybill(kWh)