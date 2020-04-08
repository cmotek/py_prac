from graphics import *

def main():

    win = GraphWin("Chart")

    infileName = input("What is the dang filename?:")
    infile = open(infileName, "r")

    numofgrades = infile.readline()
    print(numofgrades)
    gradelist = infile.readlines()
    print(gradelist)
    numbertext = Text(Point(100,100), '0 1 2 3 4 5 6 7 8 9 10')
    numbertext.draw(win)

    zeroes = gradelist.count('0\n')
    ones = gradelist.count('1\n')
    twos = gradelist.count('2\n')
    threes = gradelist.count('3\n')
    fours = gradelist.count('4\n')
    fives = gradelist.count('5\n')
    sixes = gradelist.count('6\n')
    sevens = gradelist.count('7\n')
    eights = gradelist.count('8\n')
    nines = gradelist.count('9\n')
    tens = gradelist.count('10\n')

    countlist = [zeroes, ones, twos, threes, fours, fives, sixes, sevens, eights, nines, tens]

    print(countlist)
    x = 49

    for i in countlist:
        bar = Rectangle(Point(x,82), Point(x,82-i))
        bar.setFill("black")
        bar.draw(win)
        x = x + 10
        



main()
