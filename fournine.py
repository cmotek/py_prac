from graphics import *
import math

def main():
    win = GraphWin("fournine")
    point1 = win.getMouse()
    point2 = win.getMouse()
    Rectangle(point1, point2).draw(win)
    length = abs(point2.getY() - point1.getY())
    width = abs(point2.getX() - point1.getX())
    area = length * width
    print(area)
    perimeter = 2 * (length + width)
    print(perimeter)





main()
