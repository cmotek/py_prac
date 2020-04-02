




def main():
    print("This program calculates the future value")
    print("of a 10-year investment")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    years = eval(input("How many years we talking here?"))

    print("Year         Value")
    print("____________________")
                    

    for i in range(years):
        principal = principal * (1 + apr)
        print(str(i) + "         {0:0.5f}  ".format(principal))

    
















main()
