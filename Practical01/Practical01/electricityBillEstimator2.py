
TARRIF_11 = 0.244618
TARRIF_31 = 0.136928

print("Electricity bill estimator")
print()

tarif = input("Which tarif?  11 or 31: ")

print(tarif)

if tarif != "11" and tarif != "31":
    print("Invalid Tarif Entered!")
else:
    if tarif == "11":
        cents_per_kwh = TARRIF_11
    elif tarif == "31":
        cents_per_kwh = TARRIF_31
    daily_use = float(input("Enter daily use in kWh: "))
    billing_days = int(input("Enter number of billing days: "))

    estimated_bill = cents_per_kwh * daily_use * billing_days

    print()
    print("Estimated bill: $" + str(estimated_bill))