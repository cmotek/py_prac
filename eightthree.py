

def main():



    print("This program calculates how long it takes")
    print("a 1000 dollar prinicpal to double with a given interest rate.")

    
    rate = eval(input("Enter the annual interest rate: "))

    years = 0
    totalprincipal = 1000
    init_principal = 1000

    while totalprincipal < init_principal * 2:
        totalprincipal = (totalprincipal + (totalprincipal * (rate)))
        print("calculating", totalprincipal, years)
        years = years + 1

    print("The amount of years it takes the principal to double is", years)





main()
