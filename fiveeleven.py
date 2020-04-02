


def main():
    print("This program illustrates a chaotice function")
    firstvalue = float(input("Enter a number between firstvalue: "))
    secondvalue = float(input("Enter a number between secondvalue: "))
    rangevalue = input("Enter the range:")


    print("index    " + str(firstvalue) + "     " + str(secondvalue))
    print("____________________________")




    for i in range(int(rangevalue)):
        firstvalue = 3.9 * firstvalue * (1 - firstvalue)
        secondvalue = 3.9 * secondvalue * (1 - secondvalue)
        print(str(i) + "  {0:0.5f}       {1:0.5f}  ".format(firstvalue, secondvalue))



















main()
