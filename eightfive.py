import math

def main():

    print("Is this number prime?")


    startnumber = eval(input("Enter a number greater than 2:"))

    counter = 2

    while counter <= math.sqrt(startnumber):


        if startnumber % counter != 0:
            counter = counter + 1
        elif startnumber % counter == 0:
            print("This is not a prime number at all!")
            break
            
    if counter > math.sqrt(startnumber):
        print("Holy moly it's a prime number")

    





main()
