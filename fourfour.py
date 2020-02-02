from graphics import *


def main():
    win = GraphWin()
    win.setBackground("cyan")
    ground = Rectangle(Point(0, 150), Point(200, 200))
    ground.setFill("white")
    ground.draw(win)
    face = Circle(Point(100,100), 10)
    face.setOutline("black")
    face.setFill("white")
    face.draw(win)
    belly = Circle(Point(100, 125), 15)
    belly.setOutline("black")
    belly.setFill("white")
    belly.draw(win)d
    legs = Circle(Point(100, 165), 25)
    legs.setOutline("black")
    legs.setFill("white")
    legs.draw(win)
    tree = Polygon(Point(20, 20), Point(5, 135), Point(35, 135))
    tree.setOutline("black")
    tree.setFill("green")
    tree.draw(win)
    bark = Rectangle(Point(15, 135), Point(25, 185))
    bark.setOutline("black")
    bark.setFill("brown")
    bark.draw(win)
    
    






main()
