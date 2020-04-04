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

    #x = 49
    #y = 82

    #point1 = (49,82)
    #point2 = (52,82)

    print(countlist)
    x = 49

    for i in countlist:
        bar = Rectangle(Point(x,82), Point(x,82-i))
        bar.setFill("black")
        bar.draw(win)
        x = x + 10
        
        #print(point1,point2, i)
        #point1 = point1.move(0,5)
        #print(point1)
        #print(point1.move(0,i))
        #point1.move(0,int(i))
        #point2.move(0,int(i))
        #bar = Rectangle(point1,Point(,))
        #bar = bar.move(0,5)
        #print(bar)
        #bar.setWidth(4)
        #bar.setFill('black')
        #bar.draw(win)
        #bar.move(5,i)



main()
