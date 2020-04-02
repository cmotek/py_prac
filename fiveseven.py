





def main():
    cipher = input("Please input the message to be coded:")
    newcipher = ""
    for i in cipher:
        newvalue = chr(ord(i) + 2)
        newcipher = newcipher + newvalue
    print(newcipher)



















main()
