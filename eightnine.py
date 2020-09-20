


def main():

    print("This program computes the fuel efficiency of a multi-leg journey")

    initodometer = eval(input("Please enter the intial odometer reading:"))
    legtotal = 0
    gastotal = 0 
    mpglist = []
    
    moredata = "Yes"

    while moredata == "Yes":
        legsection, gasoline = eval(input("What's your total miles for this trip and how much gas did you use?: "))
        
        leglength = legsection - initodometer
        initodometer = initodometer + leglength
        mpg = leglength / gasoline
        mpglist.append(mpg)
        legtotal = legtotal + leglength
        gastotal = gastotal + gasoline
        moredata = input("Do you have more data? (say Yes if Yes):")
     

        

    print(mpglist)
    print(str(legtotal/gastotal) + "MILES PER GALLON")

        
        








main()
