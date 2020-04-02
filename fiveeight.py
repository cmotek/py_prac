



def main():
   

    cipher = input("Please input the message to be ciphered:")
    newcipher = []
    savedvalue = 0
    codeletters = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    modeletters = "Z abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXY"
    for ch in cipher:
        savedvalue = codeletters.find(ch)
        newcipher.append(modeletters[savedvalue])
    print("".join(newcipher))


main()


















main()
