


def main():
    print("This program illustrates a chaotice function")
    firstvalue = input("Enter a number between firstvalue: ")
    secondvalue = input("Enter a number between secondvalue: ")
    rangevalue = input("Enter the range:")


    print("index    " + firstvalue + "     " + secondvalue)
    print("____________________________")




    for i in range(int(rangevalue)):
        firstprint = 3.9 * int(firstvalue) * (1 - int(firstvalue))
        secondprint = 3.9 * int(secondvalue) * (1 - int(secondvalue))
        print(i)



















main()
