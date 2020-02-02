from graphics import *

def main():
    win = GraphWin()
    princput = Entry(Point(40,40), 5)
    principal = princput.getText()
    princput.draw(win)
    invesput = Entry(Point(60,60), 5)
    investment = investput.getText()
    invesput.draw(win)
    







    #print("This program calculates the future value")
    #print("of a 10-year investment")
    #principal = eval(input("Enter the initial principal: "))
    #investment = eval(input("Enter the investment added to the principal on a yearly basis: "))
    #apr = eval(input("Enter the annual interest rate: "))
    #years = eval(input("Enter the amount of years for the interest to accrue: "))

    for i in range(years):
        principal = (principal + investment) + (apr * principal)

    #print("The value in ", years, "is:", principal)



main()
