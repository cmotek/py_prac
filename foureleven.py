from graphics import *
import math

def main():
    win = GraphWin("foureleven")
    point1 = win.getMouse()
    point2 = win.getMouse()
    Rectangle(point1, point2).draw(win)
    point3 = Point(point2.getX(), point1.getY())
    side = abs(point1.getX() - point3.getX())
    sidefifth = side/5
    sidehalffifth = sidefifth/2
    print(sidehalffifth)
    point4 = win.getMouse()
    doortop = Line(Point((point4.getX() - sidehalffifth),point4.getY()), Point((point4.getX() + sidehalffifth),point4.getY()))
    doortop.draw(win)
    doorsideone = Line(Point((point4.getX() - sidehalffifth),point4.getY()), Point((point4.getX() - sidehalffifth), point1.getY()))
    doorsideone.draw(win)
    doorsidetwo = Line(Point((point4.getX() + sidehalffifth),point4.getY()), Point((point4.getX() + sidehalffifth), point1.getY()))
    doorsidetwo.draw(win)
    point5 = win.getMouse()
    windowside = sidehalffifth/2
    window = Rectangle(Point((point5.getX() - windowside),(point5.getY() - windowside)), Point((point5.getX() + windowside),(point5.getY() + windowside)))
    window.draw(win)
    point6 = win.getMouse()
    roofsideone = Line(Point(point1.getX(), point2.getY()), point6)
    roofsideone.draw(win)
    roofsidetwo = Line(point6, point2)
    roofsidetwo.draw(win)


main()
