


def main():

    possibleleapyear = int(input("Provide year for leapyear analysis:"))

    if possibleleapyear % 4 == 0 and possibleleapyear % 400 != 0:
        print("Nope this is not a leapyear at all")
    elif possibleleapyear % 4 == 0:
        print("Why this year is in fact a leap year!")
    else:
        print("No this is not a leap year")















main()
