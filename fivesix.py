




def main():
    name = input("Please enter your name for numerical evaluation:")
    name = name.split(" ")
    namestring = "".join(name).lower()
    namecount = 0
    for i in namestring:
        lettervalue = ord(i) - 96
        namecount = namecount + lettervalue
    print(namecount)
    



















main()
