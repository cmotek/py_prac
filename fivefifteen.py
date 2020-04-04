from graphics import *

def main():

    win = GraphWin("Chart")


    infileName = input("What is the dang filename?:")
    infile = open(infileName, "r")

    numofstudents = infile.readline()
    print(numofstudents)
    gradelist = infile.readlines()

    for i in gradelist:
        name, grade = i.split()
        name = str(name)
        grade = int(grade)
        print(i)
        nametext = Text(Point(20,grade), name)
        nametext.setSize(7)
        nametext.draw(win)
        rectangle = Rectangle(Point(50,grade), Point(50 + grade, grade + 3))
        rectangle.setFill("black")
        rectangle.draw(win)
        
        
      
        print(name, grade)
    





main()
