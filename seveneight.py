



def main():

    age = int(input("How old are you?:"))
    citizenship = int(input("How many years have you been a citizen?:"))

    if age >= 25 and citizenship >= 7:
        print("You can be a member of the house of representatives!")
    else:
        print("You cannot be a member of the house of representatives!")

    if age >= 25 and citizenship >= 9:
        print("You can be a senator!")
    else:
        print("You cannot be a senator!")










main()
