import math


def main():

    print("This progam finds the Greatest Common Divisor!!!")

    t,v = eval(input("Please provide two numbers for to find the GCD:"))

    def greatcommdiv(m,n):
        while m > 0:
            n,m=m,n%m
        print(n)




    greatcommdiv(t,v)
    


















main()
