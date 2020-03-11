from graphics import *
import math

def main():
    win = GraphWin("fourten")
    point1 = win.getMouse()
    point2 = win.getMouse()
    point3 = win.getMouse()
    Polygon(point1, point2, point3).draw(win)
    lineonex = point2.getX() - point1.getX()
    lineoney = point2.getY() - point1.getY()
    lengthone = math.sqrt((lineonex * lineonex) + (lineoney * lineoney))
    print(lengthone)
    linetwox = point3.getX() - point2.getX()
    linetwoy = point3.getY() - point2.getY()
    lengthtwo = math.sqrt((linetwox * linetwox) + (linetwoy * linetwoy))
    print(lengthtwo)
    linethreex = point1.getX() - point3.getX()
    linethreey = point1.getY() - point3.getY()
    lengththree = math.sqrt((linethreex * linethreex) + (linethreey * linethreey))
    print(lengththree)
    perimeter = lengthone + lengthtwo + lengththree
    print(perimeter)
    s = (lengthone + lengthtwo + lengththree)/2
    area = math.sqrt(s * (s - lengthone) * (s - lengthtwo) * (s - lengththree))
    print(area)
    
    





















main()
