

def main():
    print("This program convertas a textual message into a sequence")
    print("of numbers represetnting the Unicode encoding of the message. \n")
    message = input("Please enter the message to encode: ")
    print("\nHere are the Unicode codes:")
    for ch in message:
        print(ord(ch), end=" ")

    print()

main()
