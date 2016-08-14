
print("Electricity bill estimator")
print()

cents_per_kwh = float(input("Enter cents per kWh: "))
daily_use = float(input("Enter daily use in kWh: "))
billing_days = int(input("Enter number of billing days: "))

estimated_bill = cents_per_kwh/100 * daily_use * billing_days

print()
print("Estimated bill: $" + str(estimated_bill)