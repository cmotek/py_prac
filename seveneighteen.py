

def main():

    try:
        x1, y1 = input("Enter a point: ").split()
        x2, y2 = input("Please provide an additional point: ").split()
        SLOPE = (y2 - y1)/(x2 - x1)
        print("Here's the slope of those points FYI: " + str(SLOPE))
    except TypeError as excObj:
        if str(excObj) == "unsupported operand type(s) for -: 'str' and 'str'":
            print("Your code is too dang buggy!")

main()
