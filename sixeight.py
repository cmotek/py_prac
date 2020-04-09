import math






def main():

    x = int(input("What number do you want the square root of?"))
    guess = int(input("How many guess attempts?"))


    def guesser(guess, x):
        guess = x/2
        for i in range(x):
            guess = (guess + (x/guess))/2
            diff = math.sqrt(7) - guess
            print(guess)
            print(diff)


    guesser(guess,x)


main()
