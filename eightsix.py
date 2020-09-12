import math

def main():

    print("What numbers less than my number are prime?")


    startnumber = eval(input("Enter a number greater than 2:"))

    primecount = 2

    primelist = []

    while primecount <= startnumber:

        primetest = 2
        
        print(primetest)

        while primetest <= math.sqrt(primecount):

            if primecount % primetest != 0:
                primetest = primetest + 1
            elif primecount % primetest == 0:
                primecount = primecount + 1
                break
                
            
        if primetest > math.sqrt(primecount):
            primelist.append(primecount)
            primecount = primecount + 1
            print(primelist)

    

main()
