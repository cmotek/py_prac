

def main():


    date = input("Please provide a date in the format MM/DD/YYYY:")
    datelist = date.split("/")
    if int(datelist[0]) > 12:
        print("This month too high to be a real month!")

    elif int(datelist[1]) > 31:
        print("No month has this many days!")

    elif int(datelist[0]) == 4 or int(datelist[0]) == 6 or int(datelist[0]) == 9 or int(datelist[0]) == 11 and int(datelist[1] > 30):
        print("That's too many days for that month!")

    elif int(datelist[0]) == 2 and int(datelist[1]) > 28:
        print("This is too many days in February!")

    else:
        print("That's a real day!")







main()
