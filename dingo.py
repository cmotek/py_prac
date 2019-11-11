def hello():
    print("Dingo World!")

hello()


def main():
    print("This program illustrates a choatic function")
    x = eval(input("Enter a number between 0 and 1: "))
    z = eval(input("Enter an additional input between 0 and 1: "))
    y = eval(input("How many numbers should I print? "))
    print("input     ", x,"      ",z)
    print("___________________________")
    for i in range(y):
            x = 3.9 * x - 3.9 * x * x
            z = 3.9 * z - 3.9 * z * z
            print(x, "          ", z)
    

main()
