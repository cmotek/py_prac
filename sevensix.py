


def main():


    speedlimit = int(input("What was the speed limit?:"))
    clockedspeed = int(input("And how fast were you going?:"))
    initialfine = 50
    ninetypenalty = 200
    totalfine = 0
    if clockedspeed > speedlimit and clockedspeed > 90:
        totalfine = 50 + ((clockedspeed - speedlimit) * 5) + ninetypenalty
        print("Your penalty is:" + str(totalfine))
    elif clockedspeed > speedlimit:
        totalfine = 50 + ((clockedspeed - speedlimit) * 5)
        print("Your penalty is:" + str(totalfine))
    elif clockedspeed <= speedlimit:
        print("Good on you for not breaking the law!")

main()
