#def main():
#    print("This program calculates the future value")
#    print("of a 10-year investment")

#    principal = eval(input("Enter the initial principal: "))
#    investment = eval(input("Enter the investment added to the principal on a yearly basis: "))
#    apr = eval(input("Enter the annual interest rate: "))
#    years = eval(input("Enter the amount of years for the interest to accrue: "))

#    for i in range(years):
#        principal = (principal + investment) * (apr)

#    print("The value in ", years, "is:", principal)

#main()

def main():
    print("This program calculates the future value")
    print("of a 10-year investment")

    principal = eval(input("Enter the initial principal: "))
    rate = eval(input("Enter the annual interest rate: "))
    periods = eval(input("Enter the number of times in a year that interest accrues: "))

    for i in range(10):
        principal = (principal + (principal * ((rate/periods) * periods)))

    print("The value in is:", principal)

main()
