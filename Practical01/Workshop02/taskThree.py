# Discount Calculator

DISCOUNT_PERCENT = .20  # .2 is 20%

def main():
    full_price = float(input("Enter Full Price: "))
    discounted_price = calculate_discount(full_price)
    print("Discounted Price: ", discounted_price)


def calculate_discount(full_price):
    discounted_price = full_price - full_price * DISCOUNT_PERCENT
    return discounted_price

main()
