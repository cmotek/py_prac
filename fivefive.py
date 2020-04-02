



def main():
    name = input("Please enter your name for numerical evaluation:")
    name = name.lower()
    namecount = 0
    for i in name:
        lettervalue = ord(i) - 96
        namecount = namecount + lettervalue
    print(namecount)
    



















main()
