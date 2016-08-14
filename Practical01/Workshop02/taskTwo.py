# Pay calculator
HOURLY_RATE = 24.95

def main():
    hours_worked = float(input("Enter Hours Worked: "))
    total_pay = calculate_pay(hours_worked)
    print("Total Pay: ",total_pay)


def calculate_pay(hours_worked):
    return hours_worked * HOURLY_RATE

main()