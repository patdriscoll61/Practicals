def main():
    house_cost = int(input("Enter the cost of the house: "))
    land_size = int(input("Enter the size of the land: "))
    land_cost = int(input("Enter the cost of the land: "))

    total_land_cost = land_size * land_cost
    total_cost = total_land_cost + house_cost

    print(total_cost)

main()
