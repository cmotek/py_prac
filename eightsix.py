import math

def main():

    print("What numbers less than my number are prime?")


    startnumber = eval(input("Enter a number greater than 2:"))

    primecount = 2

    primelist = []

    for i in range(startnumber):

        print(i)
        while primecount <= math.sqrt(i):

            if i % primecount != 0:
                primecount = primecount + 1
            elif i % primecount == 0:
                print("This is not a prime number!")
                pass

        if primecount > math.sqrt(i):
            primelist.append(i)
            print(primelist)

                

   # counter = 2

   # while counter <= math.sqrt(startnumber):


   #     if startnumber % counter != 0:
   #         counter = counter + 1
   #     elif startnumber % counter == 0:
   #         print("This is not a prime number at all!")
   #         break
            
   # if counter > math.sqrt(startnumber):
   #     print("Holy moly it's a prime number")

    

      

            


 


main()
