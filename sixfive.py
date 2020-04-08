
import math


def main():

    def squareinchpizza(diameter):
        return math.pi * ((diameter/2)**2) 


    def costperinch(c):
        return c / squareinchpizza(d)



    d = int(input("Please provide the diameter of this pizza:"))
    c = int(input("Please provide the cost of the pizza:"))



    print(squareinchpizza(d))
    print(costperinch(c))




main()
