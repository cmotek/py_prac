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

    for i in range(10):
        
        




main()
