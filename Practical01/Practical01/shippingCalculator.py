"""

Enter number of items to ship
Enter in price for each item

Calculate Total Shipping Cost
Apply discount if shipping cost > 100

"""

number_of_items = 1

while number_of_items != 0:

    number_of_items = int(input("Number of Items: "))

    if number_of_items < 0:
        print("Invalid Number of Items!")
    elif number_of_items > 0:

        total_shipping_cost = 0

        for i in range(1,number_of_items+1,1):
            item_-shipping_cost = float(input("Enter Shipping Cost for Item " + str(i) + ": "))
            total_shipping_cost = total_shipping_cost + item_shipping_cost

        if total_shipping_cost > 100:
            total_shipping_cost = total_shipping_cost - total_shipping_cost * 10 / 100
        print("Total Shipping Cost:", total_shipping_cost)