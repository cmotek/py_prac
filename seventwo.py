


def main():
    quizscore = int(input("Please input your quiz score on a scale from 0 - 5:"))
    if quizscore == 5:
        print("You got an A!")
    if quizscore == 4:
        print("You got a B!")
    if quizscore == 3:
        print("You got a C!")
    if quizscore == 2:
        print("You got a D!")
    if quizscore <= 1:
        print("You failed the test")
    


main()
