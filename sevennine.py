



def main():
    theyear = int(input("What is the year?:"))
    if theyear < 1982 or theyear > 2048:
        print("This year is outside the range of our Easter function")
    else:
        a = theyear%19
        b = theyear%4
        c = theyear%7
        d = ((19*a) + 24)%30
        e = ((2*b)+(4*c)+(6*d)+5)%7
        Easter = 22 + d + e
        if Easter > 31:
            Easter = Easter - 31
            print("Easter was on April, " + str(Easter) + " for the year " + str(theyear) + "." )
        else:
            print("Easter was on March, " + str(Easter) + " for the year " + str(theyear) + "." )



main()
