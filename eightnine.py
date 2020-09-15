


def main():

    print("This program computes the fuel efficiency of a multi-leg journey")

    initodometer = eval(input("Please enter the intial odometer reading:"))
    legtotal = 0
    gastotal = 0 
    mpglist = []
    legsection = "maleg"

    while legsection != "":
        legsection, gasoline = input("What's your total miles for this trip and how much gas did you use?: ")
        if legsection == "":
            break
        legsection = legsection
        gasoline = gasoline
        leglength = legsection - initodometer
        initodometer = initodometer + legsection
        mpg = leglength / gasoline
        mpglist.append(mpg)
        legtotal = legtotal + leglength
        gastotal = gastotal + gasoline
     

        

       
        

        

    print(mpglist)
    print(str(legtotal/gastotal) + "MILES PER GALLON")

        
        








main()
