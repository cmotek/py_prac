




def main():
    quizscore = int(input("Please input your quiz grade:"))
    if quizscore >= 90:
        print("You got an A!")
    if quizscore < 90 and quizscore >= 80:
        print("You got a B!")
    if quizscore < 80 and quizscore >= 70:
        print("You got a C!")
    if quizscore < 70 and quizscore >= 60:
        print("You got a D!")
    if quizscore < 60:
        print("You failed the test")
    


main()
