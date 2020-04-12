


def main():

    hoursworked = int(input("Please enter the hours worked a week:"))
    hourlyrate = int(input("Please enter the hourly rate:"))
    totalweeklywages = 0
    if hoursworked > 40:
        totalweeklywages = hoursworked * (hourlyrate * 1.5)
        print(totalweeklywages)
    if hoursworked <= 40:
        totalweeklywages = hoursworked * (hourlyrate)
        print(totalweeklywages)
    if hoursworked == 0:
        print("You must not have worked at all this week!")
        
        





main()
