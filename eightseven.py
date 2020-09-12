import math
import sys


def main():


    print("Lets do a Goldbach conjecture!")


    startnumber = eval(input("Enter a number for the Goldbach test:"))


    if startnumber % 2 != 0:
        print("This is not an even number! It fails the first test!")
        sys.exit()
    else:
        print("Well at least we got an even number on our hands...")
        


    primecount = 2

    firstprime = 0
    secondprime = 0
    
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
            firstprime = primecount
            primelist.append(firstprime)
            print(primelist)
            secondprime = startnumber - firstprime

            print(secondprime)
            primetest = 2

            while primetest <= math.sqrt(secondprime):

                if secondprime % primetest != 0:
                    primetest = primetest + 1
                elif secondprime % primetest == 0:
                    primelist.clear()
                    break
        
            if primetest > math.sqrt(secondprime):
                primelist.append(secondprime)
                print(primelist)
                break
            else:
                primecount = primecount + 1




main()
