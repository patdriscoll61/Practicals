
TARIF = {"11": 0.244618, "31": 0.136928}

print("Electricity bill estimator")
print()

tarifs = [tarif for tarif in TARIF.keys()]
# print(tarifs)
# tarif = input("Which tarif? {}".format(tarif for tarif in TARIF.keys()))

tarif = input("Which tarif? {}".format(tarifs))

print(tarif)

if tarif != "11" and tarif != "31":
    print("Invalid Tarif Entered!")
else:
    cents_per_kwh = TARIF[tarif]
    daily_use = float(input("Enter daily use in kWh: "))
    billing_days = int(input("Enter number of billing days: "))

    estimated_bill = cents_per_kwh * daily_use * billing_days

    print()
    print("Estimated bill: $" + str(estimated_bill))