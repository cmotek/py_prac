




def main():

    def Eastermaker(year):
        a = year%19
        b = year%4
        c = year%7
        d = ((19*a) + 24)%30
        e = ((2*b)+(4*c)+(6*d)+5)%7
        Easter = 22 + d + e
        return Easter

    
    theyear = int(input("What is the year?:"))
    
    if theyear == 1954 or theyear == 1981 or theyear == 2049 or theyear == 2076:
        Easter = Eastermaker(theyear) - 7
        if Easter > 31:
            Easter = Easter - 31
            print("Easter was on April, " + str(Easter) + " for the year " + str(theyear) + "." )
        else:
            print("Easter was on March, " + str(Easter) + " for the year " + str(theyear) + "." )
            
    else:
        if Eastermaker(theyear) > 31:
            Easter = Eastermaker(theyear) - 31
            print("Easter was on April, " + str(Easter) + " for the year " + str(theyear) + "." )
        else:
            Easter = Eastermaker(theyear)
            print("Easter was on March, " + str(Easter) + " for the year " + str(theyear) + "." )



main()
