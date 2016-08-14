def main():
    x = float(input("Enter x: "))
    y = float(input("Enter y: "))

    dummy = do_math(x,y)


def do_math(lhs,rhs):
    sum_value = lhs + rhs
    diff = lhs - rhs
    prod = lhs * rhs
    quotient = lhs / rhs

    print("Sum: ", sum_value, "Difference:", diff, "Product:", prod, "Quotient:", quotient)

main()
